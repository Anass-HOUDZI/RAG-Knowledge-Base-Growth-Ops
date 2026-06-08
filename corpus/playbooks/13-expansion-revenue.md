# Playbook Expansion Revenue (Upsell / Cross-sell)

## Contexte et objectif

L'expansion revenue est le moteur principal de la croissance nette chez **OrbitalData**. Avec un taux de rétention brute de 92 %, l'enjeu est de transformer la base clients existante en source de croissance en augmentant l'ARPU via l'upsell (montée en gamme) et le cross-sell (vente de produits complémentaires). Objectif : atteindre un NRR (Net Revenue Retention) de 115 % d'ici la fin de l'année.

## Définitions

- **Upsell** : migration d'un client vers un plan supérieur ou ajout de sièges/volume sur le plan actuel
- **Cross-sell** : vente d'un module ou produit complémentaire au produit principal
- **Expansion MRR** : revenu additionnel généré par les clients existants (hors new business)

## Signaux d'expansion

### Signaux produit (automatisés)

| Signal | Type | Score |
|---|---|---|
| Utilisation > 80 % du quota du plan actuel | Upsell | +25 |
| Tentative d'accès à une feature du plan supérieur | Upsell | +30 |
| Ajout de 3+ utilisateurs en 30 jours | Upsell | +20 |
| Utilisation d'une intégration liée à un module cross-sell | Cross-sell | +20 |
| Export de données dans un format compatible avec le module analytics | Cross-sell | +15 |

### Signaux commerciaux (manuels)

| Signal | Type | Score |
|---|---|---|
| Mention d'un besoin complémentaire lors d'un QBR | Cross-sell | +25 |
| Demande de devis pour des sièges additionnels | Upsell | +35 |
| Nouvelle équipe/département exprime un intérêt | Cross-sell | +30 |
| Renouvellement à venir dans les 60 jours | Upsell | +15 |

## Processus d'expansion

### Phase 1 — Détection (automatisée)

1. Le système de scoring calcule un **Expansion Score** pour chaque compte (0-100)
2. Les comptes avec un score ≥ 50 sont automatiquement ajoutés à la vue "Expansion Pipeline" dans le CRM
3. Notification Slack dans `#expansion-alerts` avec contexte : score, signaux déclencheurs, plan actuel

### Phase 2 — Qualification (CSM)

1. Le CSM responsable du compte valide l'opportunité sous 48h
2. **Check-list de qualification** :
   - ☐ Le besoin est confirmé (pas uniquement un signal produit)
   - ☐ Le champion interne est identifié
   - ☐ Le budget additionnel est accessible
   - ☐ Le timing est favorable (pas de gel budgétaire, pas de restructuration)
3. Si qualifié → création d'un deal "Expansion" dans le CRM avec les informations contextuelles

### Phase 3 — Exécution (CSM + AE)

1. Le CSM programme un appel avec le champion pour présenter la proposition de valeur
2. **Approche consultative** : démontrer le ROI de l'expansion basé sur l'usage actuel
   - "Vous utilisez déjà 85 % de votre quota — voici ce que le plan supérieur débloque"
   - "Votre équipe X utilise déjà le module A — le module B s'intègre nativement"
3. Proposition commerciale envoyée avec pricing détaillé et scénario ROI
4. L'AE intervient pour la négociation si le montant dépasse 10 000 € d'ACV additionnel

### Phase 4 — Clôture et activation

1. Signature de l'avenant ou upgrade en self-service
2. Activation du nouveau plan ou module dans les 24h
3. Session d'onboarding dédiée pour les nouvelles fonctionnalités
4. Tag `expansion_YYYY-MM` ajouté au deal dans le CRM

## Motions d'expansion par type de produit

| Produit | Motion upsell | Motion cross-sell |
|---|---|---|
| Plan Starter | Migration vers Pro (plus de sièges, features avancées) | Module Reporting |
| Plan Pro | Migration vers Enterprise (SSO, SLA, support dédié) | Module Analytics, Module API |
| Module Reporting | Ajout de dashboards custom | Module Data Export |

## Métriques clés

| KPI | Cible | Fréquence |
|---|---|---|
| NRR (Net Revenue Retention) | ≥ 115 % | Mensuel |
| Expansion MRR / MRR total | ≥ 8 % | Mensuel |
| Taux de conversion expansion qualifiée → close | ≥ 45 % | Mensuel |
| Délai moyen qualification → close (expansion) | < 25 jours | Mensuel |
| % base clients avec au moins 1 expansion / an | ≥ 30 % | Annuel |

---

Tags: `expansion`, `upsell`, `cross-sell`, `NRR`, `revenue`, `ARPU`, `customer-success`, `pipeline`
