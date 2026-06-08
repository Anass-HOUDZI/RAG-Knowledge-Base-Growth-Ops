# Documentation API Contacts HubSpot

**Tags :** `hubspot`, `API`, `contacts`, `REST`, `intégration`, `growth-ops`
**Dernière mise à jour :** 2026-05-18
**Auteur :** Équipe Growth Ops — ScaleUp Corp

---

## Contexte

L'API Contacts HubSpot permet d'interagir programmatiquement avec la base de contacts du CRM. Chez ScaleUp Corp, nous l'utilisons pour synchroniser les données produit, enrichir les profils contacts et automatiser les mises à jour en temps réel depuis notre stack technique.

## Authentification

Toutes les requêtes API nécessitent un token d'accès OAuth 2.0 ou une clé API privée (dépréciée).

```bash
# Authentification via Bearer Token
curl -H "Authorization: Bearer {access_token}" \
     "https://api.hubspot.fictif.com/crm/v3/objects/contacts"
```

> **⚠️ Sécurité :** Ne jamais stocker le token dans le code source. Utiliser un gestionnaire de secrets (ex. : HashiCorp Vault, AWS Secrets Manager).

## Endpoints principaux

### 1. Lister les contacts

```http
GET /crm/v3/objects/contacts
```

**Paramètres de requête :**

| Paramètre | Type | Description |
|-----------|------|-------------|
| `limit` | integer | Nombre de résultats (max 100) |
| `after` | string | Curseur de pagination |
| `properties` | string | Propriétés à inclure (séparées par virgules) |

**Exemple de requête :**

```bash
curl "https://api.hubspot.fictif.com/crm/v3/objects/contacts?limit=10&properties=email,firstname,lastname,lifecyclestage,hubspot_score" \
  -H "Authorization: Bearer {token}"
```

**Exemple de réponse :**

```json
{
  "results": [
    {
      "id": "82451",
      "properties": {
        "email": "marie.dupont@growthflow.fictif.com",
        "firstname": "Marie",
        "lastname": "Dupont",
        "lifecyclestage": "marketingqualifiedlead",
        "hubspot_score": "67"
      },
      "createdAt": "2026-03-15T10:30:00.000Z",
      "updatedAt": "2026-05-10T14:22:00.000Z"
    }
  ],
  "paging": {
    "next": {
      "after": "82452",
      "link": "https://api.hubspot.fictif.com/crm/v3/objects/contacts?after=82452"
    }
  }
}
```

### 2. Créer un contact

```http
POST /crm/v3/objects/contacts
```

**Corps de requête :**

```json
{
  "properties": {
    "email": "jean.martin@acme-corp.fictif.com",
    "firstname": "Jean",
    "lastname": "Martin",
    "company": "ACME Corp",
    "phone": "+33 6 12 34 56 78",
    "lifecyclestage": "lead",
    "lead_source": "organic_search",
    "utm_campaign": "q2_2026_content"
  }
}
```

**Réponse (201 Created) :**

```json
{
  "id": "82467",
  "properties": {
    "email": "jean.martin@acme-corp.fictif.com",
    "firstname": "Jean",
    "lastname": "Martin",
    "createdate": "2026-05-18T09:15:00.000Z"
  }
}
```

### 3. Mettre à jour un contact

```http
PATCH /crm/v3/objects/contacts/{contactId}
```

```json
{
  "properties": {
    "lifecyclestage": "salesqualifiedlead",
    "hubspot_owner_id": "45892",
    "last_qualification_date": "2026-05-18"
  }
}
```

### 4. Rechercher des contacts

```http
POST /crm/v3/objects/contacts/search
```

```json
{
  "filterGroups": [
    {
      "filters": [
        {
          "propertyName": "lifecyclestage",
          "operator": "EQ",
          "value": "marketingqualifiedlead"
        },
        {
          "propertyName": "hubspot_score",
          "operator": "GTE",
          "value": "50"
        }
      ]
    }
  ],
  "sorts": [
    {
      "propertyName": "hubspot_score",
      "direction": "DESCENDING"
    }
  ],
  "properties": ["email", "firstname", "lastname", "hubspot_score"],
  "limit": 20
}
```

### 5. Supprimer un contact

```http
DELETE /crm/v3/objects/contacts/{contactId}
```

> **⚠️ RGPD :** Pour une suppression conforme au RGPD (droit à l'oubli), utiliser l'endpoint dédié de purge GDPR plutôt que la suppression standard.

## Limites et quotas API

| Plan | Requêtes/seconde | Requêtes/jour |
|------|-------------------|---------------|
| Starter | 10/s | 250 000 |
| Pro | 15/s | 500 000 |
| Enterprise | 20/s | 1 000 000 |

## Gestion des erreurs

| Code | Signification | Action recommandée |
|------|--------------|-------------------|
| 401 | Token expiré | Rafraîchir le token OAuth |
| 409 | Contact existant (doublon email) | Utiliser l'endpoint de mise à jour |
| 429 | Rate limit atteint | Implémenter un backoff exponentiel |
| 500 | Erreur serveur HubSpot | Retry après 30 secondes |

---

*Document interne — ScaleUp Corp Growth Ops*
