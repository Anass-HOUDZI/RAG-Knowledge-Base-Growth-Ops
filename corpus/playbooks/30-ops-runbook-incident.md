# Runbook Incidents Ops Growth

## Contexte
Ce runbook est la procédure d'urgence à suivre par l'équipe Growth Ops chez ScaleUp Corp en cas d'incident technique impactant les opérations marketing ou de vente (ex: synchronisation CRM cassée, formulaires d'inscription en erreur, envois d'emails de masse accidentels).

## Classification des Incidents (Sévérité)

*   **P1 (Critique) :** Interruption totale d'un canal d'acquisition majeur (ex: formulaires du site down, sync HubSpot-Salesforce arrêtée bloquant les deals). Réponse immédiate requise 24/7.
*   **P2 (Majeur) :** Fonctionnalité importante dégradée, mais contournement possible. Impact sur un sous-ensemble d'utilisateurs. (ex: Lead scoring ne se met plus à jour). Résolution dans la journée.
*   **P3 (Mineur) :** Bug cosmétique, erreur sur un système non critique. (ex: erreur de variable de personnalisation dans un email interne). Résolution dans le sprint.

## Procédure de Gestion (Incident P1 ou P2)

### 1. Détection et Triage (Minutes 0-15)
*   **Alerte :** Réception d'une alerte Datadog, d'un ticket Support, ou constatation interne.
*   **Création du canal de crise :** Créer un channel Slack temporaire `#inc-YYYYMMDD-description` (ex: `#inc-20261105-hubspot-sync-down`).
*   **Assignation du Lead :** Une personne est nommée "Incident Commander". C'est elle qui centralise la communication.

### 2. Mitigation et Contournement (Minutes 15-60)
*   L'objectif premier n'est pas de réparer la cause profonde, mais de **stopper l'hémorragie**.
*   *Exemples d'actions immédiates :*
    *   Si une séquence d'emails s'emballe : Mettre la campagne en pause dans HubSpot.
    *   Si le formulaire d'inscription bug : Déployer un bandeau d'alerte sur le site ou basculer vers un formulaire de secours (Typeform).
    *   Si la sync de données corrompt le CRM : Désactiver le webhook de synchronisation.

### 3. Résolution et Restauration
*   Investigation de la cause profonde (Logs applicatifs, historique d'exécution des workflows).
*   Application d'un correctif.
*   Restauration des données si nécessaire (ex: relancer la synchronisation des leads bloqués manuellement).

### 4. Post-Mortem (Dans les 72h)
*   Rédaction d'un document récapitulatif (RCA - Root Cause Analysis).
*   **Structure du RCA :** Qu'est-ce qui s'est passé ? Pourquoi ? (Technique des 5 Pourquoi). Comment l'avons-nous résolu ? Comment empêcher que cela se reproduise ?
*   Création de tickets Jira pour les actions correctives à long terme.

## Contacts d'Urgence
*   Support HubSpot (via le portail partenaire)
*   Equipe Data Engineering (Astreinte) : `@data-oncall` sur Slack
*   VP Revenue Ops : Pour l'escalade des incidents impactant le chiffre d'affaires.

Tags: ops, incident-management, hubspot, troubleshooting, runbook
