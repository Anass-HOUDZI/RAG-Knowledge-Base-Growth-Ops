# Configuration du Lead Scoring (MQL/SQL)

## Contexte et objectif

Chez **GrowthFlow SaaS**, l'équipe Growth Ops a mis en place un système de lead scoring afin de prioriser les leads entrants et de qualifier automatiquement les contacts en MQL (Marketing Qualified Lead) puis en SQL (Sales Qualified Lead). Ce playbook décrit la méthodologie complète pour configurer, calibrer et maintenir le modèle de scoring dans le CRM.

## Prérequis

- Accès administrateur au CRM (propriétés personnalisées, workflows)
- Historique de conversion sur au moins 6 mois (minimum 200 deals closés)
- Alignement Sales/Marketing sur les définitions MQL et SQL

## Étapes de configuration

### 1. Définir les critères démographiques (Fit Score)

| Critère | Points | Exemple |
|---|---|---|
| Taille entreprise 50-500 employés | +15 | ICP principal |
| Taille entreprise 500+ employés | +20 | ICP premium |
| Taille entreprise < 10 employés | -10 | Hors cible |
| Poste décisionnaire (C-level, VP) | +20 | CEO, CTO, VP Sales |
| Poste opérationnel (Manager) | +10 | Marketing Manager |
| Secteur SaaS / Tech | +15 | Cible prioritaire |
| Secteur hors cible | -15 | Associations, ONG |
| Pays francophone | +5 | France, Belgique, Suisse |

### 2. Définir les critères comportementaux (Engagement Score)

| Action | Points | Decay |
|---|---|---|
| Visite page pricing | +20 | 30 jours |
| Téléchargement livre blanc | +10 | 45 jours |
| Participation webinar | +15 | 30 jours |
| Ouverture email (x3 en 7 jours) | +5 | 14 jours |
| Clic email CTA | +8 | 21 jours |
| Demande de démo | +30 | 60 jours |
| Visite page carrières | -20 | 90 jours |
| Désabonnement newsletter | -30 | Permanent |

### 3. Configurer les seuils de qualification

- **MQL** : Score total ≥ 50 points (Fit + Engagement combinés)
- **SQL** : Score total ≥ 80 points ET au moins un critère d'intention forte (visite pricing, demande démo)
- **Disqualifié** : Score négatif ou critère d'exclusion (concurrent, étudiant, email personnel)

### 4. Implémenter dans le CRM

1. Créer les propriétés personnalisées : `lead_score_fit`, `lead_score_engagement`, `lead_score_total`
2. Configurer les workflows de calcul automatique
3. Créer les vues filtrées pour l'équipe Sales : "Nouveaux MQL", "MQL → SQL en attente"
4. Activer les notifications Slack pour chaque nouveau SQL

### 5. Calibrer le modèle (itération mensuelle)

1. Extraire les leads convertis vs non-convertis des 90 derniers jours
2. Calculer le taux de conversion par tranche de score (0-25, 25-50, 50-75, 75-100)
3. Ajuster les pondérations si le taux MQL→SQL est inférieur à 25 %
4. Documenter les changements dans le changelog du scoring

## Métriques clés

| KPI | Cible | Fréquence |
|---|---|---|
| Taux MQL → SQL | ≥ 25 % | Mensuel |
| Taux SQL → Opportunity | ≥ 40 % | Mensuel |
| Volume MQL / mois | 150-300 | Mensuel |
| Précision du scoring (% SQL réellement qualifiés) | ≥ 70 % | Trimestriel |
| Temps moyen MQL → SQL | < 5 jours | Mensuel |

## Erreurs fréquentes à éviter

- Ne pas inclure de critère de decay temporel → scores gonflés sur des leads inactifs
- Pondérer trop fortement les ouvertures d'email (signal faible)
- Ne jamais recalibrer le modèle après le lancement initial
- Ignorer les signaux négatifs (visites page carrières, emails personnels)

---

Tags: `lead-scoring`, `MQL`, `SQL`, `CRM`, `qualification`, `scoring-model`, `sales-marketing-alignment`, `workflow`
