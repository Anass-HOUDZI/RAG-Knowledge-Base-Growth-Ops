# Framework d'Expérimentation Growth

## Contexte et objectif

L'expérimentation est le moteur de la croissance chez **HorizonLabs**. Plutôt que de se fier à l'intuition, l'équipe Growth opère un processus structuré de génération d'hypothèses, de priorisation, de test et d'apprentissage. Ce framework garantit la rigueur statistique, la rapidité d'exécution et la capitalisation sur les résultats. Objectif : exécuter 8-12 expérimentations par trimestre avec un taux de succès d'au moins 30 %.

## Processus en 5 étapes

### Étape 1 — Génération d'hypothèses

Chaque hypothèse suit le format standardisé :

```
Si nous [action/changement], 
alors [métrique cible] va [augmenter/diminuer] de [X %],
parce que [raisonnement basé sur des données ou insights].
```

**Exemple** :
> Si nous ajoutons un témoignage client sur la page d'inscription,
> alors le taux de conversion visiteur → inscription va augmenter de 10 %,
> parce que 68 % des prospects déclarent que la preuve sociale influence leur décision.

**Sources d'hypothèses** :
- Analyse des données produit (drop-off funnels, heatmaps, session recordings)
- Feedback utilisateurs (interviews, tickets support, NPS verbatims)
- Benchmark concurrentiel (analyse des meilleures pratiques du secteur)
- Idées de l'équipe (brainstorm mensuel ouvert à toutes les fonctions)

### Étape 2 — Priorisation (framework ICE)

Chaque hypothèse est scorée sur 3 dimensions (1 à 10) :

| Dimension | Description | Question clé |
|---|---|---|
| **I**mpact | Effet attendu sur la métrique cible | "Quel serait l'impact si ça marchait ?" |
| **C**onfiance | Niveau de certitude que l'hypothèse est correcte | "À quel point sommes-nous sûrs que ça va marcher ?" |
| **E**ase | Facilité de mise en œuvre (temps, ressources) | "Combien de temps et d'effort pour tester ?" |

```
ICE Score = (Impact + Confidence + Ease) / 3
```

**Règle** : les 3-4 hypothèses avec le meilleur score ICE sont sélectionnées pour le sprint d'expérimentation (2 semaines).

**Exemple de backlog priorisé** :

| # | Hypothèse | I | C | E | ICE | Statut |
|---|---|---|---|---|---|---|
| EXP-042 | Témoignage sur page inscription | 7 | 6 | 9 | 7.3 | ✅ Sélectionnée |
| EXP-043 | Simplification du setup (5→3 étapes) | 9 | 7 | 4 | 6.7 | ✅ Sélectionnée |
| EXP-044 | Chat proactif à J3 du trial | 6 | 5 | 8 | 6.3 | ✅ Sélectionnée |
| EXP-045 | Nouveau pricing tier | 8 | 4 | 3 | 5.0 | En attente |

### Étape 3 — Design du test

Pour chaque expérimentation sélectionnée, documenter :

1. **Hypothèse** : formulation standardisée
2. **Métrique primaire** : la métrique principale mesurée (1 seule)
3. **Métriques secondaires** : métriques complémentaires surveillées
4. **Métrique garde-fou** : métrique qui ne doit pas se dégrader (ex : NPS, taux de bug)
5. **Type de test** : A/B test, A/B/C, multivarié, before/after
6. **Taille d'échantillon requise** : calculée pour une puissance statistique de 80 % et un seuil de significativité de 95 %
7. **Durée estimée** : basée sur le trafic et la taille d'échantillon
8. **Critère de décision** : quelle amélioration justifie un déploiement ? (minimum detectable effect)

### Étape 4 — Exécution et monitoring

1. Déploiement du test via l'outil de feature flagging
2. **Monitoring quotidien** pendant les 3 premiers jours (détection d'anomalies)
3. **Pas de lecture des résultats avant la durée minimale** → éviter le "peeking bias"
4. Arrêt anticipé uniquement si la métrique garde-fou se dégrade de plus de 10 %

### Étape 5 — Analyse et décision

| Résultat | Action |
|---|---|
| Significatif et positif (p < 0.05) | Déploiement à 100 % + documentation |
| Non significatif | Clôture du test + documentation des learnings |
| Significatif mais négatif | Arrêt immédiat + analyse des causes |
| Résultat ambigu | Extension du test ou re-design |

## Documentation des résultats

Chaque expérimentation terminée est documentée dans le **Growth Experiment Log** :

```
## EXP-042 — Témoignage sur page inscription

- Hypothèse : [...]
- Dates : 15 mars — 5 avril 2025
- Variantes : Contrôle (sans témoignage) vs Test (avec témoignage vidéo)
- Résultat : +12,4 % taux d'inscription (p = 0.023)
- Décision : ✅ Déployé le 8 avril 2025
- Learnings : La vidéo courte (< 30 sec) performe mieux que le texte seul
```

## Métriques clés

| KPI | Cible | Fréquence |
|---|---|---|
| Nombre d'expérimentations / trimestre | 8-12 | Trimestriel |
| Taux de succès (tests significativement positifs) | ≥ 30 % | Trimestriel |
| Vélocité (délai idée → résultats) | < 4 semaines | Par test |
| % tests avec documentation complète | 100 % | Trimestriel |
| Impact cumulé sur la métrique North Star | Mesuré | Trimestriel |

---

Tags: `expérimentation`, `A/B-test`, `ICE`, `growth-hacking`, `hypothèse`, `framework`, `data-driven`, `optimisation`
