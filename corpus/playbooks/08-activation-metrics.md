# Métriques d'Activation Produit

## Contexte et objectif

L'activation est la première étape critique après l'acquisition : c'est le moment où un nouvel utilisateur perçoit la valeur du produit pour la première fois. Chez **PixelForge**, l'équipe Growth Product a formalisé un framework de métriques d'activation pour mesurer, optimiser et prédire la rétention à long terme. Ce document sert de référence pour toutes les équipes (Product, Growth, Engineering, Data).

## Définitions clés

- **Activation** : le moment où un utilisateur réalise une action démontrant qu'il a compris et expérimenté la valeur core du produit
- **Aha Moment** : l'instant précis de prise de conscience de la valeur — souvent corrélé à une action spécifique mesurable
- **Time-to-Value (TTV)** : le délai entre l'inscription et l'activation
- **Setup Moment** : les étapes techniques préalables à l'activation (configuration du compte, import de données)

## Framework d'activation PixelForge

### Étape 1 — Identifier l'Aha Moment

Méthodologie utilisée :

1. Extraire les cohortes d'utilisateurs inscrits entre janvier et juin 2025 (n = 8 400)
2. Segmenter en deux groupes : retenus à J30 vs non-retenus
3. Analyser les différences d'usage dans les 7 premiers jours
4. Identifier les actions corrélées à la rétention via analyse de corrélation

**Résultat** : les utilisateurs qui réalisent les 3 actions suivantes dans les 7 jours ont un taux de rétention J30 de 68 % (vs 14 % pour les autres) :

| Action d'activation | Corrélation rétention J30 | Taux de complétion actuel |
|---|---|---|
| Créer un premier design | r = 0.72 | 61 % |
| Utiliser un template premium | r = 0.68 | 34 % |
| Partager un design avec un tiers | r = 0.81 | 22 % |

### Étape 2 — Définir les métriques d'activation

| Métrique | Formule | Cible |
|---|---|---|
| Taux d'activation J7 | Utilisateurs ayant complété les 3 actions / Inscrits totaux | ≥ 45 % |
| Time-to-Value (TTV) médian | Médiane du délai inscription → 3 actions complétées | < 3 jours |
| Taux de complétion setup | Utilisateurs ayant terminé le setup / Inscrits totaux | ≥ 80 % |
| Drop-off rate par étape | % d'utilisateurs quittant à chaque étape du funnel | Identifié par étape |
| Activation qualifiée | 3/3 actions + retour dans les 48h après activation | ≥ 30 % |

### Étape 3 — Construire le funnel d'activation

```
Inscription (100%)
    │
    ├── Setup compte complété (82%)
    │       │
    │       ├── Premier design créé (61%)
    │       │       │
    │       │       ├── Template premium utilisé (34%)
    │       │       │       │
    │       │       │       └── Design partagé (22%) ← ACTIVÉ
    │       │       │
    │       │       └── Drop-off : ne découvre pas les templates
    │       │
    │       └── Drop-off : interface trop complexe au premier usage
    │
    └── Drop-off : abandon au setup (email non vérifié, profil incomplet)
```

### Étape 4 — Optimiser chaque étape

| Étape | Taux actuel | Levier d'optimisation | Test prévu |
|---|---|---|---|
| Setup → 1er design | 61 % | Simplifier le flow de création (réduire de 5 à 3 clics) | A/B test Q3 |
| 1er design → Template | 34 % | Afficher les templates en suggestion contextuelle | A/B test Q3 |
| Template → Partage | 22 % | Ajouter un bouton "Partager" dans le flow de finalisation | A/B test Q4 |
| Partage → Retour 48h | 30 % | Notification push après partage avec preview sociale | A/B test Q4 |

## Dashboard d'activation

Le dashboard d'activation est mis à jour en temps réel et accessible dans l'outil de BI interne. Il contient :

- **Vue globale** : taux d'activation J7 par semaine, comparé à la cible
- **Vue funnel** : drop-off rate par étape avec tendance sur 4 semaines
- **Vue cohorte** : taux d'activation par cohorte hebdomadaire d'inscription
- **Vue segment** : activation par source d'acquisition, par plan, par géographie

## Métriques clés

| KPI | Cible | Fréquence |
|---|---|---|
| Taux d'activation J7 | ≥ 45 % | Hebdomadaire |
| Time-to-Value médian | < 3 jours | Hebdomadaire |
| Corrélation activation → rétention J30 | ≥ 0.65 | Trimestriel |
| Impact des tests d'optimisation | ≥ +5 % par test significatif | Par test |

---

Tags: `activation`, `métriques`, `aha-moment`, `time-to-value`, `funnel`, `rétention`, `product-growth`, `onboarding`
