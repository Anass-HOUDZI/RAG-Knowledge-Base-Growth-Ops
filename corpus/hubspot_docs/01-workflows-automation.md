# Guide des Workflows d'Automatisation HubSpot

**Tags :** `hubspot`, `workflows`, `automation`, `growth-ops`, `nurturing`
**Dernière mise à jour :** 2026-05-15
**Auteur :** Équipe Growth Ops — ScaleUp Corp

---

## Contexte

Les workflows HubSpot constituent le moteur central de l'automatisation marketing et commerciale chez ScaleUp Corp. Ils permettent de déclencher des actions automatiques (envoi d'emails, mise à jour de propriétés, notifications internes) en fonction du comportement des contacts ou des événements CRM.

## Types de workflows disponibles

| Type | Déclencheur | Cas d'usage principal |
|------|------------|----------------------|
| Basé sur les contacts | Propriété ou activité contact | Nurturing, scoring |
| Basé sur les deals | Changement de stage pipeline | Alertes commerciales |
| Basé sur les tickets | Création/modification ticket | Support client |
| Basé sur les entreprises | Propriété entreprise | ABM, enrichissement |
| Planifié (cron) | Date/heure fixe | Rapports hebdomadaires |

## Configuration pas à pas

### 1. Créer un nouveau workflow

1. Aller dans **Automatisation > Workflows**
2. Cliquer sur **Créer un workflow** > **À partir de zéro**
3. Choisir le type d'objet (Contact, Deal, Entreprise…)
4. Définir les critères d'inscription

### 2. Définir les critères d'inscription

```text
Exemple : Inscrire les contacts qui remplissent TOUTES ces conditions :
  - Lifecycle Stage = MQL
  - Source originale = Organic Search
  - Pays = France OU Belgique
  - N'a PAS été inscrit dans ce workflow auparavant
```

> **⚠️ Bonne pratique :** Toujours cocher « Réinscrire les contacts qui remplissent à nouveau les critères » uniquement si le workflow est idempotent (ex. : mise à jour de propriété). Ne jamais activer cette option pour les workflows d'envoi d'emails.

### 3. Ajouter des actions

Les actions les plus utilisées chez ScaleUp Corp :

- **Envoyer un email** — utiliser un email de workflow (pas un email marketing classique)
- **Délai** — attendre X jours/heures avant l'action suivante
- **Branche Si/Sinon** — segmenter selon une propriété ou un comportement
- **Mettre à jour une propriété** — ex. : passer `lead_status` à `Nurturing`
- **Créer une tâche** — assigner une action au commercial
- **Webhook** — envoyer un payload JSON vers un endpoint externe

### 4. Paramétrer les branches conditionnelles

```text
Branche Si/Sinon :
  SI le contact a ouvert l'email "Onboarding Step 1" :
    → Envoyer "Onboarding Step 2"
  SINON :
    → Attendre 3 jours
    → Renvoyer "Onboarding Step 1" (objet modifié)
```

### 5. Configurer les paramètres de suppression

Exclure systématiquement :
- Les contacts avec `email_opt_out = true`
- Les contacts au lifecycle stage `Customer` (sauf workflow de rétention)
- Les adresses email contenant `@test.` ou `@example.`

## Bonnes pratiques

1. **Nommer clairement** : Préfixer par le canal et l'objectif — ex. `[MKT] Nurturing MQL > SQL France`
2. **Limiter la profondeur** : Un workflow ne doit pas dépasser 15 étapes. Au-delà, créer un second workflow chaîné.
3. **Journaliser** : Activer les logs d'exécution et vérifier les métriques d'inscription/désinscription chaque semaine.
4. **Tester avant activation** : Utiliser la fonctionnalité « Tester avec un contact » en environnement sandbox.
5. **Documenter** : Ajouter une note interne dans la description du workflow avec le lien Notion associé.

## Pièges courants

| Piège | Impact | Solution |
|-------|--------|----------|
| Critères trop larges | Contacts non qualifiés inscrits | Ajouter des filtres négatifs |
| Pas de suppression list | Emails envoyés à des désabonnés | Configurer la liste de suppression |
| Workflow circulaire | Boucles infinies | Vérifier les critères de réinscription |
| Délais trop courts | Emails perçus comme spam | Minimum 48h entre deux envois |

## Métriques à suivre

- **Taux d'inscription** : nombre de contacts entrant dans le workflow / contacts éligibles
- **Taux de complétion** : contacts ayant terminé toutes les étapes / inscrits
- **Taux de conversion MQL → SQL** : objectif ≥ 18% chez ScaleUp Corp
- **Taux de désinscription email** : alerte si > 1,5%

---

*Document interne — ScaleUp Corp Growth Ops*
