# Checklist Qualité Données CRM

## Contexte et objectif

La qualité des données CRM est le fondement de toutes les opérations Growth chez **NexaOps**. Des données corrompues, incomplètes ou dupliquées entraînent des erreurs de scoring, des séquences de nurturing mal ciblées et des rapports trompeurs. Ce playbook définit les standards de qualité, les contrôles automatisés et les procédures de remédiation pour maintenir un taux de conformité supérieur à 95 %.

## Dimensions de la qualité des données

| Dimension | Définition | Exemple de problème |
|---|---|---|
| **Complétude** | Tous les champs obligatoires sont remplis | Contact sans nom d'entreprise |
| **Exactitude** | Les données reflètent la réalité | Taille d'entreprise erronée |
| **Unicité** | Pas de doublons | Même contact enregistré 3 fois |
| **Cohérence** | Les données sont uniformes | "FR" vs "France" vs "france" |
| **Fraîcheur** | Les données sont à jour | Poste occupé depuis 2019, jamais mis à jour |
| **Conformité** | Les données respectent les règles RGPD | Contact sans base légale documentée |

## Checklist de contrôle (exécution mensuelle)

### 1. Complétude

- ☐ **% contacts avec email valide** : vérifier que ≥ 98 % des contacts actifs ont un email
- ☐ **% contacts avec nom d'entreprise** : cible ≥ 95 %
- ☐ **% deals avec montant renseigné** : cible 100 %
- ☐ **% deals avec source renseignée** : cible 100 %
- ☐ **% contacts avec lifecycle stage** : cible ≥ 98 %

### 2. Exactitude

- ☐ **Validation email** : lancer une vérification email en masse trimestrielle (taux de bounce cible < 3 %)
- ☐ **Enrichissement automatique** : vérifier que l'outil d'enrichissement met à jour les firmographiques mensuellement
- ☐ **Audit aléatoire** : vérifier manuellement 50 contacts tirés au sort (exactitude attendue ≥ 90 %)

### 3. Unicité (dédoublonnage)

- ☐ **Scan de doublons** : lancer le détecteur de doublons sur les critères suivants :
  - Même email
  - Même nom + même entreprise
  - Même numéro de téléphone
- ☐ **Fusion des doublons** : fusionner les doublons détectés selon les règles de fusion :
  - Le contact le plus ancien est le master
  - Les propriétés vides du master sont complétées par le doublon
  - Les activités et notes sont consolidées
- ☐ **Cible** : < 2 % de doublons dans la base active

### 4. Cohérence

- ☐ **Normalisation des pays** : tous les pays en code ISO 2 lettres (FR, BE, CH)
- ☐ **Normalisation des secteurs** : utilisation de la liste fermée de 20 secteurs définis
- ☐ **Normalisation des postes** : mapping des titres libres vers les catégories standard (C-level, VP, Manager, IC)
- ☐ **Devises** : tous les montants en EUR, conversion automatique si nécessaire

### 5. Fraîcheur

- ☐ **Contacts inactifs** : identifier les contacts sans aucune activité depuis 12 mois
- ☐ **Données firmographiques obsolètes** : re-enrichir les contacts n'ayant pas été mis à jour depuis 6 mois
- ☐ **Deals stagnants** : identifier les deals sans mise à jour depuis 60 jours → alerte au pipeline manager

### 6. Conformité RGPD

- ☐ **Base légale documentée** : vérifier que chaque contact a une base légale (consentement, intérêt légitime, contrat)
- ☐ **Opt-out respecté** : aucun contact désabonné ne doit être inscrit dans une séquence email active
- ☐ **Droit à l'oubli** : vérifier que les demandes de suppression ont été traitées sous 30 jours
- ☐ **Registre des traitements** : mise à jour du registre si nouveaux traitements ajoutés

## Automatisation des contrôles

### Workflows de qualité automatisés

| Workflow | Fréquence | Action |
|---|---|---|
| Détection contacts sans email | Quotidien | Tag `data_quality_no_email` + exclusion des séquences |
| Détection doublons | Hebdomadaire | Notification dans `#data-quality` avec liste |
| Validation email bounce | Après chaque envoi | Marquage `email_invalid` si hard bounce |
| Normalisation pays | Temps réel | Conversion automatique vers ISO 2 lettres |
| Alerte deals stagnants | Hebdomadaire | Notification au deal owner après 45 jours sans mise à jour |

## Métriques clés

| KPI | Cible | Fréquence |
|---|---|---|
| Taux de complétude global | ≥ 95 % | Mensuel |
| Taux de doublons dans la base | < 2 % | Mensuel |
| Taux de bounce email | < 3 % | Mensuel |
| Taux de conformité RGPD | 100 % | Trimestriel |
| Score de qualité global (composite) | ≥ 90/100 | Mensuel |

---

Tags: `data-quality`, `CRM`, `RGPD`, `dédoublonnage`, `normalisation`, `hygiène-données`, `conformité`, `enrichissement`
