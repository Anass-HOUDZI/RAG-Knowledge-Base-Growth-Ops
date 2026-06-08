# Optimisation du Channel Mix

## Contexte et objectif

L'optimisation du channel mix est un exercice stratégique critique chez **VelocityGrowth** pour maximiser le retour sur investissement marketing global. Plutôt que d'optimiser chaque canal en silo, l'équipe Growth adopte une approche portfolio : allouer le budget entre les canaux pour maximiser le volume de clients acquis à un CAC cible. Ce playbook décrit la méthodologie d'analyse, les critères de décision et le processus de réallocation.

## Framework d'analyse du channel mix

### Matrice de performance par canal

Chaque canal est évalué sur 4 dimensions :

| Dimension | Question | Mesure |
|---|---|---|
| **Volume** | Combien de leads/clients ce canal génère-t-il ? | Nombre de MQL, clients acquis |
| **Qualité** | Les leads de ce canal convertissent-ils bien ? | Taux MQL→Client, LTV |
| **Coût** | Combien coûte l'acquisition sur ce canal ? | CAC, CPL |
| **Scalabilité** | Ce canal peut-il absorber plus de budget sans dégrader le CAC ? | Courbe de rendement marginal |

### Catégorisation des canaux

| Catégorie | Caractéristiques | Exemples | Stratégie |
|---|---|---|---|
| **Fondation** | CAC bas, volume élevé, long à construire | SEO, contenu, communauté | Investir en continu |
| **Accélération** | CAC modéré, scalable, résultats rapides | Ads (LinkedIn, Google), webinars | Augmenter si ROI > seuil |
| **Expérimental** | Potentiel inconnu, petit budget test | Podcasts, partenariats, TikTok B2B | Tester avec budget limité (< 10 %) |
| **Maturité** | CAC en hausse, rendements décroissants | Canal historique saturé | Optimiser ou réduire |

## Processus de réallocation budgétaire

### Étape 1 — Audit mensuel des performances

Extraire les métriques suivantes pour chaque canal :

```
| Canal           | Budget | Leads | MQL  | Clients | CAC    | LTV/CAC | Tendance CAC |
|-----------------|--------|-------|------|---------|--------|---------|-------------|
| SEO/Content     | 8 000€ | 1 800 | 290  | 45      | 178€   | 8,5:1   | Stable       |
| LinkedIn Ads    | 15 000€| 1 200 | 210  | 32      | 469€   | 3,8:1   | ↗️ +5%      |
| Google Ads      | 12 000€| 900   | 120  | 15      | 800€   | 2,7:1   | ↗️ +12%     |
| Parrainage      | 2 000€ | 600   | 95   | 22      | 91€    | 11,2:1  | Stable       |
| Événements      | 10 000€| 200   | 45   | 8       | 1 250€ | 2,1:1   | Stable       |
```

### Étape 2 — Analyse de la courbe de rendement marginal

Pour chaque canal, tracer la courbe **budget → nombre de clients acquis** sur les 6 derniers mois :

- **Rendement croissant** : le canal absorbe plus de budget efficacement → augmenter
- **Rendement constant** : le CAC est stable quelle que soit l'augmentation → maintenir ou augmenter prudemment
- **Rendement décroissant** : le CAC augmente avec le budget → plafonner ou réduire

### Étape 3 — Réallocation

**Règle du 70-20-10** :
- **70 %** du budget sur les canaux fondation + accélération prouvés (ROI > 3:1)
- **20 %** sur les canaux en optimisation (ROI 2-3:1, potentiel d'amélioration)
- **10 %** sur les canaux expérimentaux (budget test, aucune garantie de ROI)

### Étape 4 — Exécution et monitoring

1. Valider la nouvelle allocation lors du comité Growth mensuel
2. Communiquer les changements aux channel managers avec les objectifs révisés
3. Monitoring hebdomadaire du pacing (budget consommé vs budget prévu)
4. Alerte automatique si le CAC d'un canal dépasse 120 % de la cible

## Signaux de décision

| Signal | Action |
|---|---|
| CAC d'un canal augmente de > 15 % sur 2 mois consécutifs | Réduire le budget de 20 %, investiguer les causes |
| Nouveau canal expérimental avec ROI > 3:1 sur 3 mois | Augmenter le budget de 50 %, passer en "Accélération" |
| LTV/CAC d'un canal passe sous 2:1 | Mettre en pause, auditer la qualité des leads |
| Canal fondation atteint un plateau de volume | Investir dans le contenu et la diversification des mots-clés |

## Métriques clés

| KPI | Cible | Fréquence |
|---|---|---|
| CAC blended (tous canaux) | < 55 € | Mensuel |
| LTV/CAC blended | ≥ 4:1 | Trimestriel |
| % budget sur canaux à ROI > 3:1 | ≥ 70 % | Mensuel |
| Diversification (aucun canal > 40 % du budget) | Respecté | Mensuel |
| Nombre de canaux testés / trimestre | ≥ 2 nouveaux | Trimestriel |

---

Tags: `channel-mix`, `budget`, `CAC`, `ROI`, `acquisition`, `allocation`, `rendement-marginal`, `marketing-analytics`
