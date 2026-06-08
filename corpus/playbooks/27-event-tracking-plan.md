# Plan de Tracking des Événements Produit

## Contexte
Pour optimiser le funnel PLG (Product-Led Growth) de GrowthFlow, il est crucial de collecter des données comportementales fiables. Ce document définit les standards pour le tracking des événements dans l'application via Segment.

## Conventions de Nommage
Nous utilisons la structure `Objet Action` (en anglais, format PascalCase) :
*   **Objet :** L'élément du produit avec lequel l'utilisateur interagit (ex: `Project`, `User`, `Report`).
*   **Action :** Le verbe décrivant ce qui s'est passé (ex: `Created`, `Updated`, `Deleted`, `Viewed`).

Exemples valides : `Project Created`, `Report Exported`, `Subscription Upgraded`.
Exemples invalides : `create_project`, `User clicked on export`.

## Événements Core à Tracker Obligatoirement

### 1. Cycle de vie utilisateur
*   `User Signed Up` (Propriétés : `method` (email, google), `utm_source`)
*   `User Logged In`
*   `Workspace Created`

### 2. Activation (Aha Moment)
*   `First Dashboard Viewed`
*   `Data Source Connected` (Propriétés : `integration_name`, `status`)
*   `First Query Run`

### 3. Monétisation
*   `Trial Started` (Propriétés : `plan_name`)
*   `Subscription Upgraded` (Propriétés : `old_plan`, `new_plan`, `mrr_increase`)
*   `Subscription Cancelled` (Propriétés : `reason`)

## Processus d'Implémentation d'un Nouvel Événement

1.  **Demande (Product Manager) :** Le PM soumet un ticket Jira décrivant l'événement souhaité et le business context.
2.  **Validation (Data/Growth Ops) :** Vérification du nommage et définition précise des propriétés à associer.
3.  **Implémentation (Dev) :** Ajout du code de tracking `analytics.track()` dans l'app.
4.  **QA (Data) :** Vérification dans Segment Debugger que l'événement remonte correctement en staging.
5.  **Mise en prod et documentation :** Déploiement et mise à jour du dictionnaire de données interne.

## KPIs Liés au Tracking
*   Pourcentage d'événements mal formés (monitoring via Segment Protocols)
*   Nombre d'événements orphelins (trackés mais non utilisés dans des dashboards)

Tags: tracking, data, segment, product-led-growth, analytics
