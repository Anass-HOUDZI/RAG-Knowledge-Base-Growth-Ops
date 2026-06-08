# Séquence d'Onboarding Nouveaux Utilisateurs

## Contexte et objectif

L'onboarding est le moment critique où un nouvel utilisateur découvre la valeur du produit. Chez **NovaPulse**, l'équipe Growth a conçu une séquence d'onboarding en 14 jours combinant emails automatisés, notifications in-app et accompagnement humain conditionnel. L'objectif est d'amener 60 % des nouveaux inscrits à atteindre leur "Aha Moment" (première action à valeur ajoutée) dans les 7 premiers jours.

## Définition du "Aha Moment"

Après analyse des cohortes Q1–Q3 2025, l'équipe Data a identifié que les utilisateurs qui réalisent **3 actions clés dans les 7 premiers jours** ont un taux de rétention J30 de 72 % contre 18 % pour les autres :

1. **Créer un premier projet** (activation primaire)
2. **Inviter un collaborateur** (effet réseau)
3. **Publier un premier livrable** (valeur délivrée)

## Séquence détaillée

### Jour 0 — Inscription

- **Email de bienvenue** : envoyé immédiatement après la création du compte
  - Objet : "Bienvenue sur NovaPulse — votre premier projet en 2 minutes"
  - Contenu : lien direct vers la création de projet, vidéo tutoriel (45 sec)
  - CTA principal : "Créer mon premier projet"
- **Notification in-app** : checklist d'onboarding affichée dans le dashboard
  - ☐ Créer un projet
  - ☐ Inviter un collaborateur
  - ☐ Publier un livrable

### Jour 1 — Relance douce

- **Email conditionnel** (envoyé seulement si le projet n'est pas créé) :
  - Objet : "Besoin d'un coup de main pour démarrer ?"
  - Contenu : 3 templates de projets prêts à l'emploi
- **Tooltip in-app** : guide interactif au survol du bouton "Nouveau projet"

### Jour 3 — Activation sociale

- **Email** : "Travaillez en équipe — invitez vos collègues"
  - Contenu : avantages du travail collaboratif, lien d'invitation pré-rempli
  - Condition : envoyé uniquement si l'utilisateur a créé un projet mais n'a pas invité de collaborateur

### Jour 5 — Valeur délivrée

- **Email** : "Publiez votre premier livrable en 3 clics"
  - Contenu : guide pas-à-pas avec captures d'écran
  - Condition : projet créé, collaborateur invité, mais aucun livrable publié

### Jour 7 — Point de bascule

- **Email récapitulatif** : résumé de l'avancement dans la checklist
  - Si 3/3 actions complétées : email de félicitations + offre upgrade
  - Si < 3/3 : proposition d'un appel de 15 minutes avec un Customer Success Manager
- **Notification in-app** : badge "Early Adopter" débloqué si 3/3 complétées

### Jour 10 — Engagement continu

- **Email** : fonctionnalités avancées adaptées au comportement observé
  - Utilisateur actif → intégrations tierces, API
  - Utilisateur peu actif → cas d'usage concrets par secteur

### Jour 14 — Bilan onboarding

- **Email de clôture** : "Votre premier mois avec NovaPulse"
  - Statistiques d'utilisation personnalisées
  - Invitation à rejoindre la communauté utilisateurs
  - Enquête NPS intégrée (1 question)

## Règles de segmentation

| Segment | Critère | Traitement |
|---|---|---|
| Power User | 3/3 actions en < 3 jours | Fast-track vers séquence d'expansion |
| Standard | 3/3 actions en 4-7 jours | Séquence complète |
| À risque | < 2/3 actions à J7 | Escalade vers CSM |
| Inactif | 0 action à J3 | Email de réactivation + appel sortant |

## Métriques clés

| KPI | Cible | Fréquence |
|---|---|---|
| Taux d'activation J7 (3/3 actions) | ≥ 60 % | Hebdomadaire |
| Taux d'ouverture emails onboarding | ≥ 55 % | Hebdomadaire |
| Taux de clic CTA principal | ≥ 18 % | Hebdomadaire |
| Rétention J30 (activés vs non-activés) | ≥ 70 % vs baseline | Mensuel |
| NPS J14 | ≥ 45 | Mensuel |

---

Tags: `onboarding`, `activation`, `email-sequence`, `aha-moment`, `rétention`, `product-led-growth`, `user-journey`
