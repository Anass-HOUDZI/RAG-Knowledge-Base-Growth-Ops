# Intégration Webhooks et Synchronisation Externe

**Tags :** `hubspot`, `webhooks`, `intégration`, `API`, `sync`, `n8n`, `growth-ops`
**Dernière mise à jour :** 2026-05-22
**Auteur :** Équipe Growth Ops — ScaleUp Corp

---

## Contexte

L'intégration de HubSpot avec les outils externes est essentielle pour maintenir une source de vérité unique chez ScaleUp Corp. Ce document décrit l'architecture d'intégration par webhooks, les flux de synchronisation en place et les bonnes pratiques pour garantir la fiabilité des données.

## Architecture d'intégration

```
┌─────────────┐     Webhook      ┌──────────────┐     ETL      ┌──────────────┐
│   HubSpot   │ ───────────────► │   n8n Cloud  │ ──────────► │  Data        │
│   CRM       │                  │   (iPaaS)    │             │  Warehouse   │
│             │ ◄─────────────── │              │ ◄────────── │  (BigQuery)  │
└─────────────┘   API REST       └──────────────┘   Reverse   └──────────────┘
                                        │            ETL
                                        │
                                        ▼
                                 ┌──────────────┐
                                 │   Slack      │
                                 │   Alerts     │
                                 └──────────────┘
```

## Webhooks HubSpot → Externe

### Configuration des webhooks

1. **Paramètres > Intégrations > API privée > Webhooks**
2. Définir l'URL cible (endpoint n8n ou serveur personnalisé)
3. Sélectionner les événements à surveiller
4. Configurer la signature de vérification (HMAC SHA-256)

### Événements configurés

| Événement | Payload | Destination | Action déclenchée |
|-----------|---------|------------|-------------------|
| `contact.creation` | Contact complet | n8n → BigQuery | Insertion dans `raw_hubspot_contacts` |
| `contact.propertyChange` | Propriété modifiée | n8n → BigQuery | Mise à jour incrémentale |
| `deal.creation` | Deal complet | n8n → Slack | Notification `#new-deals` |
| `deal.propertyChange` (stage) | Nouveau stage | n8n → BigQuery + Slack | Mise à jour pipeline + alerte |
| `contact.propertyChange` (lifecyclestage) | Nouveau stage | n8n | Déclenchement workflow enrichissement |

### Exemple de payload webhook

```json
{
  "eventId": 1234567890,
  "subscriptionId": 456789,
  "portalId": 98765432,
  "occurredAt": 1716044400000,
  "subscriptionType": "contact.propertyChange",
  "attemptNumber": 0,
  "objectId": 82451,
  "propertyName": "lifecyclestage",
  "propertyValue": "marketingqualifiedlead",
  "changeSource": "CRM",
  "sourceId": "workflow-12345"
}
```

### Vérification de la signature

```python
import hashlib
import hmac

def verify_hubspot_signature(request_body: str, signature: str, client_secret: str) -> bool:
    """Vérifie l'authenticité d'un webhook HubSpot (v3)."""
    expected = hmac.new(
        client_secret.encode("utf-8"),
        request_body.encode("utf-8"),
        hashlib.sha256
    ).hexdigest()
    return hmac.compare_digest(expected, signature)
```

> **⚠️ Sécurité :** Toujours vérifier la signature HMAC avant de traiter un webhook. Sans vérification, un attaquant pourrait injecter de faux événements.

## Synchronisation Externe → HubSpot

### Flux de synchronisation produit

Les données produit sont synchronisées vers HubSpot toutes les 15 minutes via un script Python exécuté par un cron job.

```python
import requests

HUBSPOT_API = "https://api.hubspot.fictif.com/crm/v3/objects/contacts"
HEADERS = {
    "Authorization": "Bearer {token}",
    "Content-Type": "application/json"
}

def sync_product_data(account_id: str, usage_data: dict):
    """Synchronise les données produit vers HubSpot."""
    # Rechercher le contact par account_id
    search_payload = {
        "filterGroups": [{
            "filters": [{
                "propertyName": "prod_account_id",
                "operator": "EQ",
                "value": account_id
            }]
        }]
    }
    
    response = requests.post(f"{HUBSPOT_API}/search", json=search_payload, headers=HEADERS)
    results = response.json().get("results", [])
    
    if results:
        contact_id = results[0]["id"]
        update_payload = {
            "properties": {
                "prod_usage_score": usage_data["usage_score"],
                "prod_last_login": usage_data["last_login"],
                "prod_plan_type": usage_data["plan"],
                "prod_activation_status": usage_data["activation_status"]
            }
        }
        requests.patch(f"{HUBSPOT_API}/{contact_id}", json=update_payload, headers=HEADERS)
```

### Reverse ETL (BigQuery → HubSpot)

Les données agrégées du data warehouse sont poussées vers HubSpot pour enrichir les profils contacts :

| Donnée source | Table BigQuery | Propriété HubSpot cible | Fréquence |
|--------------|---------------|------------------------|-----------|
| Score d'usage | `mart_partner_360` | `prod_usage_score` | Toutes les 15 min |
| Segment client | `mart_partner_360` | `sc_segment` | Quotidienne |
| Revenu total | `mart_revenue_monthly` | `billing_mrr` | Quotidienne |
| Cohorte d'inscription | `mart_cohort_retention` | `sc_cohort_month` | À l'inscription |

## Gestion des erreurs

### Retry policy

HubSpot retry automatiquement les webhooks en échec selon la politique suivante :

| Tentative | Délai | Action si échec |
|-----------|-------|----------------|
| 1 | Immédiat | — |
| 2 | 1 minute | — |
| 3 | 5 minutes | — |
| 4 | 30 minutes | — |
| 5 | 4 heures | Alerte Slack |
| 6+ | Abandon | Log dans `webhook_failures` |

### Monitoring

- **Dashboard de monitoring** : Vérifier le taux de succès des webhooks dans n8n (objectif ≥ 99,5%)
- **Alertes** : Notification Slack si > 5 webhooks échouent en 1h
- **Dead letter queue** : Les payloads en échec sont stockés dans une file d'attente pour retraitement

## Bonnes pratiques

1. **Idempotence** : Chaque endpoint récepteur doit être idempotent (traiter le même événement 2 fois sans effet de bord).
2. **Timeout** : Le endpoint doit répondre en < 5 secondes. Traiter de manière asynchrone si le processing est long.
3. **Filtrage côté récepteur** : Ne pas souscrire à tous les événements. Filtrer uniquement ce qui est nécessaire.
4. **Logs structurés** : Logger chaque webhook reçu avec l'`eventId`, `objectId` et le timestamp.
5. **Environnement de test** : Utiliser un portail HubSpot sandbox pour tester les intégrations avant la production.

---

*Document interne — ScaleUp Corp Growth Ops*
