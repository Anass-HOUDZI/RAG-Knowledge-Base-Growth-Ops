# Segmentation par Listes Actives et Statiques

**Tags :** `hubspot`, `listes`, `segmentation`, `ciblage`, `growth-ops`
**Dernière mise à jour :** 2026-05-05
**Auteur :** Équipe Growth Ops — ScaleUp Corp

---

## Contexte

La segmentation par listes est un pilier de la stratégie Growth de ScaleUp Corp. Elle permet de cibler précisément les audiences pour les campagnes email, les workflows d'automatisation et le reporting. HubSpot propose deux types de listes avec des comportements distincts.

## Types de listes

### Listes actives (dynamiques)

Les listes actives se mettent à jour automatiquement lorsqu'un contact remplit ou ne remplit plus les critères définis.

**Cas d'usage :**
- Ciblage de campagnes récurrentes
- Critères d'inscription de workflows
- Audiences pour le reporting en temps réel
- Synchronisation avec les plateformes publicitaires

### Listes statiques (figées)

Les listes statiques ne changent pas après leur création. Les contacts doivent être ajoutés ou retirés manuellement (ou par workflow/import).

**Cas d'usage :**
- Participants à un événement spécifique
- Contacts importés depuis un fichier
- Snapshot d'une audience à une date donnée
- Exclusion permanente (ex. : concurrents identifiés)

## Convention de nommage

```
[TYPE] | [CATÉGORIE] | Nom descriptif — Date si pertinent
```

**Exemples :**
- `[ACTIVE] | MKT | MQLs France — Score ≥ 50`
- `[STATIC] | EVENT | Participants Webinar Product Launch — 2026-04-15`
- `[ACTIVE] | SALES | SQLs Non Assignés`
- `[ACTIVE] | EXCL | Concurrents et Partenaires`

## Listes actives principales

### Segmentation par lifecycle stage

| Nom de la liste | Critères |
|----------------|----------|
| `[ACTIVE] \| FUNNEL \| Subscribers` | `lifecyclestage = subscriber` |
| `[ACTIVE] \| FUNNEL \| Leads` | `lifecyclestage = lead` |
| `[ACTIVE] \| FUNNEL \| MQLs` | `lifecyclestage = marketingqualifiedlead` |
| `[ACTIVE] \| FUNNEL \| SQLs` | `lifecyclestage = salesqualifiedlead` |
| `[ACTIVE] \| FUNNEL \| Customers` | `lifecyclestage = customer` |

### Segmentation par engagement

| Nom de la liste | Critères |
|----------------|----------|
| `[ACTIVE] \| ENG \| Actifs 30j` | A ouvert ou cliqué un email dans les 30 derniers jours |
| `[ACTIVE] \| ENG \| Inactifs 90j` | Aucune activité email ou web dans les 90 derniers jours |
| `[ACTIVE] \| ENG \| Power Users` | `prod_usage_score ≥ 80` ET `prod_last_login` < 7 jours |
| `[ACTIVE] \| ENG \| At Risk` | `prod_usage_score` en baisse de > 20% sur 30j |

### Segmentation par géographie et segment

| Nom de la liste | Critères |
|----------------|----------|
| `[ACTIVE] \| GEO \| France` | `country = France` |
| `[ACTIVE] \| GEO \| DACH` | `country IN (Germany, Austria, Switzerland)` |
| `[ACTIVE] \| SEG \| Enterprise` | `sc_segment = enterprise` ET `company_size > 500` |
| `[ACTIVE] \| SEG \| SMB` | `sc_segment = smb` ET `company_size ≤ 50` |

### Listes d'exclusion

| Nom de la liste | Critères | Usage |
|----------------|----------|-------|
| `[ACTIVE] \| EXCL \| Désabonnés` | `email_opt_out = true` | Exclure de tout envoi |
| `[ACTIVE] \| EXCL \| Bounces hard` | `email_hard_bounce = true` | Exclure de tout envoi |
| `[STATIC] \| EXCL \| Concurrents` | Ajoutés manuellement | Exclure des campagnes et du scoring |
| `[ACTIVE] \| EXCL \| Emails invalides` | Email contient `@test.` OU `@example.` | Exclure de tout envoi |

## Gestion via API

### Récupérer les contacts d'une liste

```bash
curl "https://api.hubspot.fictif.com/contacts/v1/lists/{listId}/contacts/all?count=50" \
  -H "Authorization: Bearer {token}"
```

### Ajouter des contacts à une liste statique

```bash
curl -X POST "https://api.hubspot.fictif.com/contacts/v1/lists/{listId}/add" \
  -H "Authorization: Bearer {token}" \
  -H "Content-Type: application/json" \
  -d '{"vids": [82451, 82467, 82490]}'
```

## Bonnes pratiques

1. **Limiter le nombre de listes** : Maximum 150 listes actives. Archiver les listes obsolètes mensuellement.
2. **Utiliser les listes actives par défaut** : Préférer les listes actives sauf besoin de snapshot.
3. **Ne pas imbriquer excessivement** : Éviter les listes basées sur l'appartenance à d'autres listes (maximum 2 niveaux).
4. **Tester les critères** : Vérifier le nombre de contacts avant d'utiliser une liste dans une campagne.
5. **Synchroniser avec les ads** : Utiliser les listes actives comme audiences Facebook/Google pour le retargeting.

## Métriques

- **Taille des listes** : Suivre l'évolution hebdomadaire des listes clés (MQLs, Actifs, At Risk)
- **Taux de couverture** : % de la base totale couverte par au moins une liste de segmentation
- **Taux d'exclusion** : % de contacts dans les listes d'exclusion (alerte si > 15%)

---

*Document interne — ScaleUp Corp Growth Ops*
