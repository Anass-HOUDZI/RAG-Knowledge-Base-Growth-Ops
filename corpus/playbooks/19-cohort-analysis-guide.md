# Guide d'Analyse de Cohortes

## Contexte et objectif

L'analyse de cohortes est l'outil fondamental pour comprendre le comportement des utilisateurs dans le temps chez **MeridianApp**. Contrairement aux métriques agrégées qui masquent les tendances, l'analyse de cohortes permet d'isoler les effets temporels et d'évaluer l'impact réel des changements produit ou marketing. Ce guide formalise la méthodologie, les types d'analyses et les bonnes pratiques pour l'équipe Growth.

## Qu'est-ce qu'une cohorte ?

Une **cohorte** est un groupe d'utilisateurs partageant une caractéristique commune pendant une période définie. La dimension la plus courante est la **date d'inscription** (cohorte temporelle), mais d'autres dimensions sont possibles.

### Types de cohortes

| Type | Dimension | Exemple |
|---|---|---|
| Temporelle | Semaine/mois d'inscription | "Inscrits semaine du 10 mars 2025" |
| Acquisition | Canal d'acquisition | "Inscrits via campagne LinkedIn Q1" |
| Comportementale | Action réalisée | "Utilisateurs ayant activé la feature X" |
| Plan | Type de plan | "Utilisateurs freemium vs trial vs payant" |
| Géographique | Pays/région | "Inscrits France vs Allemagne" |

## Méthodologie standard

### Étape 1 — Définir la question

Formuler clairement la question avant de construire l'analyse :

- "Le taux de rétention J30 s'améliore-t-il d'une cohorte à l'autre ?"
- "Les utilisateurs acquis via le parrainage ont-ils une meilleure rétention que ceux acquis via Ads ?"
- "L'expérimentation d'onboarding lancée en semaine 12 a-t-elle amélioré l'activation ?"

### Étape 2 — Construire la matrice de cohortes

**Exemple : matrice de rétention par cohorte mensuelle**

| Cohorte | Taille | M0 | M1 | M2 | M3 | M4 | M5 | M6 |
|---|---|---|---|---|---|---|---|---|
| Jan 2025 | 1 200 | 100 % | 42 % | 31 % | 25 % | 22 % | 20 % | 19 % |
| Fév 2025 | 1 350 | 100 % | 45 % | 34 % | 28 % | 24 % | 22 % | — |
| Mar 2025 | 1 500 | 100 % | 48 % | 37 % | 30 % | 26 % | — | — |
| Avr 2025 | 1 420 | 100 % | 51 % | 39 % | 32 % | — | — | — |
| Mai 2025 | 1 600 | 100 % | 53 % | 41 % | — | — | — | — |
| Juin 2025 | 1 550 | 100 % | 55 % | — | — | — | — | — |

**Lecture** : la cohorte de mars 2025 avait un taux de rétention de 48 % au mois 1, 37 % au mois 2, etc. La tendance montre une amélioration progressive de la rétention M1 de 42 % à 55 % sur 6 mois.

### Étape 3 — Interpréter les résultats

**Signaux positifs** :
- Les cohortes récentes ont une meilleure rétention que les anciennes → les améliorations produit portent leurs fruits
- La courbe de rétention se stabilise (plateau) → les utilisateurs restants sont fidèles

**Signaux d'alerte** :
- La rétention d'une cohorte est significativement inférieure aux précédentes → régression ou problème ponctuel
- Aucune stabilisation visible → le produit ne crée pas assez de valeur récurrente
- Taille de cohorte en baisse → problème d'acquisition

### Étape 4 — Agir sur les insights

| Insight | Action |
|---|---|
| Rétention M1 en hausse | Documenter les changements qui ont contribué, poursuivre |
| Drop-off marqué entre M0 et M1 | Renforcer l'onboarding et le nurturing J7-J30 |
| Plateau tardif (M4+) | Investiguer les features de rétention long-terme |
| Cohorte canal X sous-performante | Revoir le ciblage ou le messaging de ce canal |

## Analyses avancées

### Cohorte comportementale : impact de l'activation

Comparer la rétention entre utilisateurs activés (Aha Moment atteint) et non activés :

| Segment | Taille | M1 | M3 | M6 |
|---|---|---|---|---|
| Activés (3/3 actions J7) | 680 | 72 % | 55 % | 44 % |
| Partiellement activés (1-2/3) | 420 | 38 % | 18 % | 9 % |
| Non activés (0/3) | 300 | 12 % | 4 % | 1 % |

**Conclusion** : la différence de rétention M6 entre activés et non activés est de 43 points → l'activation est le levier prioritaire.

### Cohorte de revenu : LTV par cohorte

| Cohorte | ARPU M1 | ARPU M6 | LTV estimée (12 mois) |
|---|---|---|---|
| Q1 2025 | 28 € | 35 € | 380 € |
| Q2 2025 | 30 € | 38 € | 420 € |

## Bonnes pratiques

1. **Taille de cohorte minimale** : 100 utilisateurs pour des conclusions statistiquement fiables
2. **Granularité** : utiliser des cohortes hebdomadaires pour l'analyse fine, mensuelles pour le reporting
3. **Cohérence des définitions** : utiliser les mêmes définitions de rétention (session active vs login vs action core) dans toutes les analyses
4. **Comparaison isolée** : ne changer qu'une variable à la fois pour attribuer un effet causal

## Métriques clés

| KPI | Cible | Fréquence |
|---|---|---|
| Rétention M1 (cohorte mensuelle) | ≥ 50 % | Mensuel |
| Rétention M6 | ≥ 25 % | Mensuel |
| Amélioration rétention M1 d'une cohorte à l'autre | ≥ +1 point/mois | Mensuel |
| Couverture d'analyse (% cohortes analysées) | 100 % | Mensuel |

---

Tags: `cohortes`, `rétention`, `analytics`, `LTV`, `activation`, `product-analytics`, `data`, `segmentation`
