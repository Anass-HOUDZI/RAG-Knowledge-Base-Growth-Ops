# Définition et Scoring des Product Qualified Leads (PQL)

## Contexte et objectif

Dans un modèle Product-Led Growth, les **Product Qualified Leads (PQL)** remplacent progressivement les MQL traditionnels comme principal signal de qualification commerciale. Chez **DataPilot**, l'équipe Growth a développé un modèle PQL basé sur l'usage produit réel pour identifier les utilisateurs freemium les plus susceptibles de convertir en client payant. L'objectif : concentrer l'effort commercial sur les 15 % d'utilisateurs qui génèrent 80 % des conversions.

## Qu'est-ce qu'un PQL ?

Un PQL est un utilisateur ou un compte qui a atteint un **seuil d'engagement produit** démontrant une probabilité élevée de conversion. Contrairement au MQL (basé sur des signaux marketing), le PQL repose sur des **actions réelles dans le produit**.

## Identification des actions prédictives

L'analyse de régression logistique réalisée sur 4 200 utilisateurs freemium (cohortes S1 2025) a révélé les actions les plus prédictives de conversion :

| Action produit | Coefficient prédictif | Seuil PQL |
|---|---|---|
| Nombre de projets créés | 0.82 | ≥ 3 projets |
| Nombre d'utilisateurs invités | 0.76 | ≥ 2 invitations |
| Utilisation d'une intégration tierce | 0.71 | ≥ 1 intégration connectée |
| Nombre de sessions / semaine | 0.65 | ≥ 5 sessions |
| Utilisation feature premium (aperçu) | 0.89 | ≥ 1 tentative |
| Volume de données importées | 0.58 | ≥ 500 lignes |

## Modèle de scoring PQL

### Score composite (0-100)

```
PQL_Score = (Projets × 15) + (Invitations × 12) + (Intégrations × 18) 
          + (Sessions_hebdo × 3) + (Feature_premium × 25) + (Volume_données × 0.01)
```

**Plafonné à 100 points.**

### Seuils de qualification

| Niveau | Score | Action |
|---|---|---|
| PQL Fort | ≥ 70 | Assignation immédiate à un AE, notification Slack #pql-alerts |
| PQL Modéré | 40-69 | Séquence de nurturing in-app + email, revue hebdo par le SDR |
| Non qualifié | < 40 | Reste dans le parcours freemium, pas d'intervention commerciale |

## Processus de traitement des PQL

### PQL Fort (score ≥ 70)

1. **Notification automatique** dans le canal Slack `#pql-alerts` avec contexte enrichi :
   - Nom du compte, plan actuel, score PQL, actions réalisées
   - Lien direct vers le profil utilisateur dans le CRM
2. **L'AE assigné** contacte le champion identifié sous 24h ouvrées
3. **Approche personnalisée** basée sur l'usage observé :
   - "J'ai vu que vous avez connecté 3 intégrations — souhaitez-vous découvrir les intégrations premium ?"
4. **Tracking du cycle** : date de contact, réponse, outcome (converti, reporté, perdu)

### PQL Modéré (score 40-69)

1. Activation d'une **bannière in-app** présentant les fonctionnalités premium pertinentes
2. **Séquence email** de 3 messages sur 10 jours :
   - J0 : Cas d'usage avancé lié au comportement observé
   - J4 : Témoignage client du même secteur
   - J10 : Offre d'essai premium 14 jours
3. Si le score passe ≥ 70 pendant la séquence → bascule en PQL Fort

## Métriques clés

| KPI | Cible | Fréquence |
|---|---|---|
| Volume PQL Fort / mois | 80-120 | Mensuel |
| Taux de conversion PQL Fort → Paid | ≥ 35 % | Mensuel |
| Taux de conversion PQL Modéré → Paid | ≥ 12 % | Mensuel |
| Délai moyen PQL → Close | < 18 jours | Mensuel |
| Précision du modèle (AUC) | ≥ 0.78 | Trimestriel |

## Recalibration du modèle

- **Mensuelle** : revue des coefficients avec l'équipe Data
- **Trimestrielle** : ré-entraînement du modèle sur les données récentes
- **Ad hoc** : recalibration obligatoire après tout changement majeur du produit (nouvelle feature, refonte UX)

---

Tags: `PQL`, `product-qualified-lead`, `product-led-growth`, `scoring`, `freemium`, `conversion`, `sales-assist`
