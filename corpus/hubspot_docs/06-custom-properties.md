# Propriétés Personnalisées HubSpot

**Tags :** `hubspot`, `propriétés`, `CRM`, `data-model`, `growth-ops`
**Dernière mise à jour :** 2026-04-20
**Auteur :** Équipe Growth Ops — ScaleUp Corp

---

## Contexte

Les propriétés personnalisées étendent le modèle de données standard de HubSpot pour capturer les informations spécifiques au business de ScaleUp Corp. Ce document référence toutes les propriétés custom créées, leur convention de nommage et les bonnes pratiques associées.

## Convention de nommage

Toutes les propriétés personnalisées suivent le format :

```
{catégorie}_{nom_descriptif}
```

**Catégories :**
- `sc_` — propriétés spécifiques ScaleUp Corp
- `prod_` — données produit synchronisées
- `mkt_` — données marketing
- `sales_` — données commerciales
- `billing_` — données facturation

## Propriétés Contacts

### Données produit

| Nom interne | Label | Type | Description |
|-------------|-------|------|-------------|
| `prod_account_id` | Account ID Produit | Texte | Identifiant unique du compte dans le produit |
| `prod_signup_date` | Date d'inscription produit | Date | Date de création du compte |
| `prod_plan_type` | Plan actuel | Enum | `free`, `starter`, `pro`, `enterprise` |
| `prod_usage_score` | Score d'usage | Nombre | Score composite d'utilisation (0-100) |
| `prod_last_login` | Dernier login | Date | Date du dernier accès au produit |
| `prod_activation_status` | Statut d'activation | Enum | `not_started`, `in_progress`, `activated` |
| `prod_feature_adoption` | Features adoptées | Texte | Liste JSON des fonctionnalités utilisées |

### Données marketing

| Nom interne | Label | Type | Description |
|-------------|-------|------|-------------|
| `mkt_first_touch_channel` | Premier canal d'acquisition | Enum | `organic`, `paid`, `referral`, `partner`, `direct` |
| `mkt_lead_magnet` | Lead magnet téléchargé | Texte | Nom du contenu téléchargé initialement |
| `mkt_webinar_attended` | Webinars assistés | Nombre | Compteur de webinars auxquels le contact a participé |
| `mkt_content_score` | Score contenu | Nombre | Score basé sur la consommation de contenu |
| `mkt_utm_first_campaign` | Première campagne UTM | Texte | Valeur `utm_campaign` du premier clic |

### Données commerciales

| Nom interne | Label | Type | Description |
|-------------|-------|------|-------------|
| `sales_qualified_date` | Date de qualification SQL | Date | Date à laquelle le contact a été qualifié SQL |
| `sales_disqualification_reason` | Raison de disqualification | Enum | `no_budget`, `no_authority`, `no_need`, `no_timing` |
| `sales_icp_match` | Correspondance ICP | Enum | `strong`, `moderate`, `weak`, `excluded` |
| `sales_territory` | Territoire commercial | Enum | `france_north`, `france_south`, `benelux`, `dach` |

## Propriétés Deals

| Nom interne | Label | Type | Description |
|-------------|-------|------|-------------|
| `sc_deal_source` | Source du deal | Enum | `inbound`, `outbound`, `plg`, `partner`, `upsell` |
| `sc_arr_value` | Valeur ARR | Devise | Valeur annuelle récurrente du deal |
| `sc_competitors` | Concurrents identifiés | Texte | Liste des concurrents évalués par le prospect |
| `sc_champion_id` | Champion interne | Contact | Contact référence chez le prospect |

## Propriétés Entreprises

| Nom interne | Label | Type | Description |
|-------------|-------|------|-------------|
| `sc_segment` | Segment client | Enum | `smb`, `mid_market`, `enterprise` |
| `sc_tech_stack` | Stack technique | Texte | Technologies utilisées (enrichissement) |
| `sc_partner_tier` | Tier partenaire | Enum | `silver`, `gold`, `platinum` |
| `billing_mrr` | MRR actuel | Devise | Revenu mensuel récurrent |
| `billing_contract_end` | Fin de contrat | Date | Date de fin du contrat en cours |

## Création via API

```bash
# Créer une propriété personnalisée (endpoint fictif)
curl -X POST "https://api.hubspot.fictif.com/crm/v3/properties/contacts" \
  -H "Authorization: Bearer {token}" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "prod_usage_score",
    "label": "Score d'\''usage",
    "type": "number",
    "fieldType": "number",
    "groupName": "product_data",
    "description": "Score composite d'\''utilisation du produit, calculé quotidiennement (0-100)"
  }'
```

## Bonnes pratiques

1. **Grouper les propriétés** : Créer des groupes de propriétés (`product_data`, `marketing_data`, `sales_data`) pour organiser l'interface CRM.
2. **Limiter le nombre** : Ne pas dépasser 200 propriétés custom par objet. Auditer et archiver les propriétés inutilisées chaque trimestre.
3. **Documenter** : Chaque propriété doit avoir une description claire dans HubSpot ET dans ce document.
4. **Typage strict** : Utiliser le type le plus contraignant possible (Enum plutôt que Texte quand les valeurs sont finies).
5. **Ne jamais renommer le nom interne** : Le `name` est immuable après création. Seul le `label` peut être modifié.

## Pièges courants

- **Propriétés en doublon** : Vérifier qu'une propriété similaire n'existe pas avant d'en créer une nouvelle
- **Valeurs incohérentes** : Utiliser des enums plutôt que du texte libre pour éviter les variantes (`France` vs `france` vs `FR`)
- **Propriétés orphelines** : Supprimer les propriétés qui ne sont utilisées dans aucun workflow, rapport ou vue

---

*Document interne — ScaleUp Corp Growth Ops*
