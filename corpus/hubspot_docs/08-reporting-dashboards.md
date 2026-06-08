# Dashboards et Rapports HubSpot

**Tags :** `hubspot`, `reporting`, `dashboards`, `KPIs`, `analytics`, `growth-ops`
**Dernière mise à jour :** 2026-05-20
**Auteur :** Équipe Growth Ops — ScaleUp Corp

---

## Contexte

Les dashboards HubSpot centralisent la visibilité sur les performances Growth de ScaleUp Corp. Ce document décrit l'architecture des dashboards, les rapports configurés et les bonnes pratiques de reporting. L'objectif est que chaque équipe (Marketing, Sales, Product) ait accès à une vue pertinente et actualisée.

## Architecture des dashboards

### Dashboard 1 : Vue exécutive (C-Level)

**Audience :** CEO, CRO, CMO
**Fréquence de consultation :** Hebdomadaire

| Rapport | Type | Métrique principale |
|---------|------|---------------------|
| MRR Evolution | Graphique linéaire | MRR total + variation M/M |
| Funnel Overview | Entonnoir | Taux de conversion par stage |
| Pipeline Value | Jauge | Pipeline pondéré vs. quota |
| CAC par canal | Barres empilées | Coût d'acquisition par source |
| NRR (Net Revenue Retention) | KPI unique | % de rétention nette |

### Dashboard 2 : Marketing Performance

**Audience :** Head of Marketing, Growth Marketers
**Fréquence de consultation :** Quotidienne

| Rapport | Type | Métrique principale |
|---------|------|---------------------|
| Leads générés par source | Barres empilées | Nombre de leads par canal |
| MQL créés cette semaine | KPI + tendance | Nombre de MQLs vs. objectif |
| Performance email | Tableau | Taux d'ouverture, clic, désinscription |
| Top pages de conversion | Tableau | Pages avec le plus de soumissions formulaire |
| Attribution multi-touch | Barres | Contribution de chaque touchpoint au revenu |
| Score distribution | Histogramme | Répartition des contacts par tranche de score |

### Dashboard 3 : Sales Performance

**Audience :** Sales Manager, Account Executives, SDRs
**Fréquence de consultation :** Quotidienne

| Rapport | Type | Métrique principale |
|---------|------|---------------------|
| Pipeline par stage | Barres horizontales | Valeur par stage du pipeline |
| Deals créés vs. fermés | Double barre | Volume de création vs. closing |
| Vélocité du cycle | KPI | Durée moyenne du cycle de vente |
| Win rate par commercial | Tableau | Taux de conversion par deal owner |
| Activités commerciales | Compteurs | Appels, emails, meetings cette semaine |
| Deals at risk | Tableau filtré | Deals sans activité > 14 jours |

### Dashboard 4 : Product-Led Growth

**Audience :** Product Manager, Growth Engineer
**Fréquence de consultation :** Quotidienne

| Rapport | Type | Métrique principale |
|---------|------|---------------------|
| Signups quotidiens | Graphique linéaire | Inscriptions par jour |
| Taux d'activation | KPI | % de signups ayant complété l'activation |
| Trial → Paid conversion | Entonnoir | Taux de conversion trial vers payant |
| Usage score moyen | Graphique linéaire | Évolution du score d'usage moyen |
| Feature adoption | Barres | % d'adoption par fonctionnalité clé |

## Création d'un rapport personnalisé

### Pas à pas

1. **Rapports > Créer un rapport > Rapport personnalisé**
2. Choisir la source de données (Contacts, Deals, Activités…)
3. Sélectionner les propriétés à analyser
4. Configurer les filtres (période, segment, lifecycle stage…)
5. Choisir le type de visualisation
6. Nommer et sauvegarder dans le dashboard approprié

### Exemple : rapport de conversion MQL → SQL par canal

```text
Source de données : Contacts
Axe X : mkt_first_touch_channel
Axe Y : Nombre de contacts
Filtre : lifecyclestage = salesqualifiedlead
         createdate = ce trimestre
Segmenté par : lifecyclestage (au moment de la création)
Type : Barres empilées
```

## Rapports via API

```bash
# Récupérer les données analytics (endpoint fictif)
curl "https://api.hubspot.fictif.com/analytics/v2/reports/funnel?start=2026-01-01&end=2026-05-31" \
  -H "Authorization: Bearer {token}"
```

**Réponse :**

```json
{
  "funnel": [
    {"stage": "visitor", "count": 125000},
    {"stage": "lead", "count": 8500},
    {"stage": "mql", "count": 2100},
    {"stage": "sql", "count": 580},
    {"stage": "customer", "count": 165}
  ],
  "period": "2026-01-01/2026-05-31"
}
```

## Bonnes pratiques

1. **Un dashboard = une audience** : Ne pas mélanger les métriques C-Level et opérationnelles.
2. **Limiter à 10 rapports par dashboard** : Au-delà, le chargement ralentit et la lisibilité diminue.
3. **Période par défaut cohérente** : Configurer la période par défaut selon l'audience (hebdo pour le C-Level, quotidien pour les opérationnels).
4. **Partage contrôlé** : Utiliser les permissions de dashboard pour limiter l'accès aux données sensibles (revenus, coûts).
5. **Alertes automatiques** : Configurer des alertes email quand un KPI dépasse un seuil critique.

## Pièges courants

- **Rapports en doublon** : Centraliser les rapports pour éviter les versions contradictoires
- **Données non filtrées** : Toujours exclure les contacts internes (domaine `@scaleup-corp.fictif.com`)
- **Attribution simpliste** : Utiliser l'attribution multi-touch plutôt que le dernier clic seul

---

*Document interne — ScaleUp Corp Growth Ops*
