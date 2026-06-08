# Définition des Lifecycle Stages CRM

## Contexte et objectif

La cohérence des lifecycle stages dans le CRM est la colonne vertébrale de l'alignement Sales-Marketing chez **BridgePoint Analytics**. Ce playbook définit chaque stage, les critères de transition, les responsabilités et les règles de gouvernance pour garantir une donnée fiable et exploitable par toutes les équipes.

## Vue d'ensemble des stages

```
Abonné → Lead → MQL → SQL → Opportunity → Client → Évangéliste
                                                        ↓
                                                   Churné
```

## Définitions détaillées

### 1. Abonné (Subscriber)

- **Définition** : Contact ayant souscrit à la newsletter ou à un flux de contenu sans autre interaction
- **Critère d'entrée** : Opt-in newsletter, inscription blog
- **Propriétaire** : Marketing
- **Actions autorisées** : Envoi de contenus éducatifs uniquement (pas de communication commerciale)

### 2. Lead

- **Définition** : Contact ayant manifesté un intérêt au-delà de la simple inscription (téléchargement, participation événement, visite répétée)
- **Critère d'entrée** : Au moins 1 action d'engagement qualifiante (téléchargement de ressource, inscription webinar, formulaire de contact)
- **Propriétaire** : Marketing
- **Délai de traitement** : Enrichissement automatique dans les 24h (firmographiques, technographiques)

### 3. MQL (Marketing Qualified Lead)

- **Définition** : Lead ayant atteint le seuil de scoring défini, démontrant un fit et un engagement suffisants
- **Critère d'entrée** : Lead score ≥ 50 (cf. playbook 01-lead-scoring-setup)
- **Propriétaire** : Marketing (transmission à Sales dans les 4h)
- **SLA** : Sales doit accepter ou rejeter le MQL dans les 24h ouvrées

### 4. SQL (Sales Qualified Lead)

- **Définition** : MQL accepté par Sales après qualification manuelle (appel ou échange écrit)
- **Critère d'entrée** : MQL accepté par le SDR/AE après vérification des critères BANT :
  - **B**udget : budget identifié ou processus budgétaire en cours
  - **A**utorité : interlocuteur décisionnaire ou accès au décisionnaire confirmé
  - **N**eed : besoin explicite identifié et articulé
  - **T**imeline : projet dans les 6 prochains mois
- **Propriétaire** : Sales (AE assigné)
- **Minimum 2/4 critères BANT validés** pour passer en SQL

### 5. Opportunity

- **Définition** : SQL pour lequel un deal a été créé dans le pipeline commercial
- **Critère d'entrée** : Deal créé avec montant estimé, date de clôture prévisionnelle et stage pipeline défini
- **Propriétaire** : AE assigné
- **Champs obligatoires** : montant, date close, source, produit, nombre de sièges

### 6. Client (Customer)

- **Définition** : Contact dont le deal a été marqué "Closed Won"
- **Critère d'entrée** : Signature du contrat et/ou premier paiement reçu
- **Propriétaire** : Customer Success Manager
- **Transition automatique** : déclenchée par le workflow "Deal Closed Won"

### 7. Évangéliste (Evangelist)

- **Définition** : Client actif ayant un NPS ≥ 9 et/ou participant activement au programme de parrainage
- **Critère d'entrée** : NPS ≥ 9 sur la dernière enquête ET au moins 1 action d'advocacy (avis, témoignage, parrainage)
- **Propriétaire** : Customer Marketing

### 8. Churné (Churned)

- **Définition** : Ancien client ayant résilié son abonnement
- **Critère d'entrée** : Résiliation effective du contrat
- **Propriétaire** : Customer Success (analyse post-mortem obligatoire)

## Règles de gouvernance

- **Aucun retour en arrière** : un SQL ne peut pas redevenir un MQL (il peut être disqualifié ou mis en recycling)
- **Recyclage** : un SQL non converti après 90 jours est renvoyé en "Lead" avec tag `recycled` pour re-nurturing
- **Audit mensuel** : vérification des contacts bloqués dans un stage depuis plus de 60 jours
- **Data quality** : les contacts sans email valide ou sans nom d'entreprise sont automatiquement exclus du pipeline

## Métriques clés

| KPI | Cible | Fréquence |
|---|---|---|
| Taux de transition MQL → SQL | ≥ 25 % | Mensuel |
| Taux de transition SQL → Opportunity | ≥ 40 % | Mensuel |
| Délai moyen MQL → SQL | < 24h | Mensuel |
| % contacts sans lifecycle stage | < 2 % | Mensuel |
| Taux de recyclage SQL | < 30 % | Trimestriel |

---

Tags: `lifecycle`, `CRM`, `MQL`, `SQL`, `pipeline`, `qualification`, `BANT`, `data-governance`, `sales-marketing-alignment`
