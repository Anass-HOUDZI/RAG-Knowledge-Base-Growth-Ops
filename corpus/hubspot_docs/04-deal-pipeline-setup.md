# Configuration du Pipeline de Deals

**Tags :** `hubspot`, `deals`, `pipeline`, `sales`, `CRM`, `growth-ops`
**Dernière mise à jour :** 2026-05-02
**Auteur :** Équipe Growth Ops — ScaleUp Corp

---

## Contexte

Le pipeline de deals dans HubSpot structure le processus de vente de ScaleUp Corp. Il permet de visualiser les opportunités en cours, de prévoir le chiffre d'affaires et d'identifier les goulets d'étranglement dans le cycle de vente. Nous opérons deux pipelines distincts selon le segment client.

## Pipelines configurés

### Pipeline 1 : Self-Serve (PLG)

Destiné aux clients qui s'inscrivent et convertissent via le produit.

| Stage | Probabilité | Propriétés requises | Durée cible |
|-------|------------|---------------------|-------------|
| Trial Started | 10% | `trial_start_date`, `plan_type` | — |
| Activation | 25% | `activation_event = true` | < 3 jours |
| Engaged User | 40% | `usage_score ≥ 30` | < 7 jours |
| Upgrade Intent | 60% | Visite page pricing OU clic CTA upgrade | < 14 jours |
| Payment Initiated | 80% | Début du flow de paiement | < 1 jour |
| Closed Won | 100% | Paiement confirmé | — |
| Closed Lost | 0% | Trial expiré sans conversion | — |

### Pipeline 2 : Sales-Assisted (Enterprise)

Destiné aux comptes qualifiés nécessitant un accompagnement commercial.

| Stage | Probabilité | Propriétés requises | Durée cible |
|-------|------------|---------------------|-------------|
| Discovery Call | 10% | `discovery_date`, `deal_owner` | — |
| Qualification | 20% | `budget_confirmed`, `decision_maker_id` | < 5 jours |
| Demo Completed | 40% | `demo_date`, `demo_feedback` | < 10 jours |
| Proposal Sent | 60% | `proposal_amount`, `proposal_date` | < 7 jours |
| Negotiation | 75% | `contract_sent = true` | < 14 jours |
| Closed Won | 100% | Contrat signé | — |
| Closed Lost | 0% | Raison de perte renseignée | — |

## Configuration pas à pas

### 1. Créer un pipeline

1. **Paramètres > Objets > Deals > Pipelines**
2. Cliquer **Créer un pipeline**
3. Nommer le pipeline (ex. : `Self-Serve PLG`)
4. Ajouter les stages avec les probabilités associées

### 2. Propriétés obligatoires par stage

Pour chaque stage, configurer les propriétés requises avant de pouvoir avancer :

```text
Stage "Qualification" → Propriétés obligatoires :
  ☑ Budget confirmé (budget_confirmed)
  ☑ Décideur identifié (decision_maker_id)
  ☑ Échéance projet (project_deadline)
```

> **⚠️ Bonne pratique :** Ne pas rendre trop de propriétés obligatoires (3 maximum par stage). Un pipeline trop contraignant décourage les commerciaux de le mettre à jour.

### 3. Automatisations associées

**À la création d'un deal :**
- Assigner automatiquement le `deal_owner` selon le territoire (`region`)
- Créer une tâche de premier contact sous 4h
- Envoyer une notification Slack dans `#pipeline-updates`

**Au changement de stage :**
```text
SI deal passe en "Proposal Sent" :
  → Créer tâche manager : "Valider la proposition"
  → Envoyer email récapitulatif au contact
  → Mettre à jour propriété last_stage_change_date
```

**Au Closed Won :**
- Mettre à jour le lifecycle stage du contact → `Customer`
- Déclencher le workflow d'onboarding
- Créer un ticket de setup dans le pipeline Support

**Au Closed Lost :**
- Exiger une raison de perte (`closed_lost_reason`) parmi :
  - Budget insuffisant
  - Concurrent choisi
  - Pas de besoin immédiat
  - Pas de réponse
  - Autre (champ libre)

### 4. Règles de rotation des deals

Les deals inactifs sont gérés automatiquement :

| Condition | Action |
|-----------|--------|
| Deal en "Discovery Call" > 10 jours sans activité | Notification au deal owner |
| Deal en "Proposal Sent" > 21 jours | Relance automatique par email |
| Deal en tout stage > 45 jours sans changement | Alerte manager + revue pipeline |

## Métriques du pipeline

- **Valeur totale du pipeline** : somme pondérée par probabilité (objectif : 3x le quota)
- **Vélocité** : temps moyen par stage et durée totale du cycle
- **Win rate** : Closed Won / (Closed Won + Closed Lost) — objectif ≥ 28%
- **Deal size moyen** : segmenté par pipeline (Self-Serve vs. Enterprise)

---

*Document interne — ScaleUp Corp Growth Ops*
