# Playbook Prévention du Churn

## Contexte et objectif

Le churn est l'ennemi numéro un de la croissance durable. Chez **ScaleUp Corp**, le taux de churn mensuel était de 4,2 % en début d'année, représentant une perte annuelle de ~38 % du MRR. Ce playbook décrit le système de détection précoce, les interventions automatisées et les escalades manuelles mises en place pour ramener le churn sous la barre des 2 % mensuel.

## Signaux d'alerte (Early Warning Signals)

### Signaux produit

- Baisse de la fréquence de connexion de plus de 50 % sur 14 jours glissants
- Aucune utilisation d'une fonctionnalité core depuis 21 jours
- Suppression de données ou export massif
- Diminution du nombre d'utilisateurs actifs dans le compte (désactivations)

### Signaux commerciaux

- Ticket support non résolu depuis plus de 5 jours ouvrés
- Note CSAT ≤ 2/5 sur un ticket récent
- Absence de réponse aux 3 derniers emails du CSM
- Demande d'informations sur la procédure de résiliation

### Signaux financiers

- Échec de paiement (carte expirée, rejet bancaire)
- Downgrade de plan dans les 60 derniers jours
- Demande de remise non standard à moins de 30 jours du renouvellement

## Système de scoring du risque churn

Chaque compte reçoit un **score de risque churn** sur 100 points, recalculé quotidiennement :

| Signal | Points de risque |
|---|---|
| Connexion en baisse > 50 % (14j) | +25 |
| Aucune feature core utilisée (21j) | +20 |
| Export massif de données | +15 |
| Ticket non résolu > 5 jours | +10 |
| CSAT ≤ 2/5 | +15 |
| Échec de paiement | +10 |
| Downgrade récent | +10 |
| Demande résiliation | +30 |

**Seuils d'alerte :**
- 🟢 0-25 : Sain — monitoring standard
- 🟡 26-50 : Attention — intervention automatisée
- 🟠 51-75 : Risque élevé — escalade CSM
- 🔴 76-100 : Critique — intervention directe manager CS

## Procédures d'intervention

### Niveau 🟡 Attention (score 26-50)

1. Déclencher un email automatisé de ré-engagement avec du contenu à valeur ajoutée
2. Activer une notification in-app proposant un tutoriel sur les fonctionnalités sous-utilisées
3. Programmer un check-in automatique par le CSM dans les 5 jours ouvrés

### Niveau 🟠 Risque élevé (score 51-75)

1. Le CSM contacte le champion identifié dans le compte sous 48h
2. Organiser un "Health Check" de 30 minutes : revue de l'usage, identification des blocages
3. Proposer une session de formation personnalisée gratuite
4. Créer un plan de succès à 30 jours co-construit avec le client

### Niveau 🔴 Critique (score 76+)

1. Le Manager CS prend le lead sur le compte
2. Appel direct dans les 24h avec une offre de rétention (extension gratuite, migration, remise)
3. Escalade au VP Customer Success si le client représente plus de 5 000 € de MRR
4. Documentation post-mortem systématique si churn effectif

## Offres de rétention (arsenal)

| Offre | Condition | Approbation requise |
|---|---|---|
| 1 mois gratuit | Score ≥ 50, MRR < 2 000 € | CSM |
| 20 % de remise sur 3 mois | Score ≥ 50, MRR 2 000-5 000 € | Manager CS |
| Migration de données assistée | Problème technique identifié | CSM |
| Formation équipe offerte (2h) | Sous-utilisation démontrée | CSM |
| Remise 30 % annuelle | MRR ≥ 5 000 €, menace compétiteur | VP CS |

## Métriques clés

| KPI | Cible | Fréquence |
|---|---|---|
| Churn MRR mensuel | < 2 % | Mensuel |
| Taux de rétention nette (NRR) | ≥ 110 % | Mensuel |
| % comptes 🟠/🔴 contactés dans les SLA | ≥ 90 % | Hebdomadaire |
| Taux de save (clients retenus / clients à risque) | ≥ 40 % | Mensuel |
| Délai moyen d'intervention après alerte | < 48h | Hebdomadaire |

---

Tags: `churn`, `rétention`, `customer-success`, `health-score`, `early-warning`, `save-rate`, `NRR`, `MRR`
