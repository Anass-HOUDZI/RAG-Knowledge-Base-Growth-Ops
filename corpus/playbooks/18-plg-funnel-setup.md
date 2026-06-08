# Configuration du Funnel PLG (Product-Led Growth)

## Contexte et objectif

**ZenithBoard** a adopté un modèle Product-Led Growth où le produit lui-même est le principal vecteur d'acquisition, d'activation et de monétisation. Ce playbook décrit la configuration complète du funnel PLG, de l'inscription self-serve à la conversion payante, en passant par les mécaniques de viralité et d'expansion intégrées au produit.

## Architecture du funnel PLG

```
Visiteur → Inscription gratuite → Setup → Activation → Engagement → Monétisation → Expansion
                                                            ↓
                                                        Viralité
                                                     (Invitations)
```

## Étape 1 — Acquisition (Visiteur → Inscription)

### Landing page produit

- **CTA principal** : "Essayez gratuitement — pas de carte bancaire requise"
- **Réduction de friction** : inscription en 1 clic via SSO (Google, Microsoft)
- **Preuve sociale** : "Rejoint par 4 200 équipes" (compteur actualisé mensuellement)
- **Démo interactive** : widget embarqué permettant de tester une feature sans inscription

### Métriques acquisition

| KPI | Cible |
|---|---|
| Taux de conversion visiteur → inscription | ≥ 8 % |
| Coût par inscription (CPI) | < 5 € (canaux organiques < 1 €) |
| % inscriptions self-serve (vs assisted) | ≥ 90 % |

## Étape 2 — Setup (Inscription → Configuration)

### Flow de setup simplifié

1. **Écran 1** : "Quel est votre objectif principal ?" (3 choix max → personnalisation du dashboard)
2. **Écran 2** : "Importez vos données ou démarrez avec un template" (option skip disponible)
3. **Écran 3** : accès direct au dashboard personnalisé

**Principes** :
- Maximum 3 écrans de setup
- Chaque écran apporte de la valeur immédiate (personnalisation, contenu pré-rempli)
- Option "Skip" disponible à chaque étape — ne jamais bloquer l'accès au produit

### Métriques setup

| KPI | Cible |
|---|---|
| Taux de complétion setup | ≥ 80 % |
| Temps médian de setup | < 90 secondes |

## Étape 3 — Activation (Setup → Aha Moment)

L'activation est définie comme la réalisation de l'action qui prédit la rétention à long terme. Pour ZenithBoard :

**Aha Moment** = Créer un board + ajouter ≥ 3 cartes + inviter 1 collaborateur (dans les 7 jours)

### Leviers d'activation

- **Onboarding interactif** : guide pas-à-pas intégré au produit (3 étapes visuelles)
- **Templates intelligents** : le template proposé dépend du secteur déclaré au setup
- **Emails comportementaux** : envoyés en fonction des actions non réalisées (cf. playbook 02)
- **Nudges in-app** : tooltips et notifications contextuelles pour guider vers les actions d'activation

## Étape 4 — Engagement (Activation → Usage régulier)

### Définition de l'engagement

Un utilisateur est considéré "engagé" s'il réalise ≥ 3 sessions par semaine avec ≥ 1 action substantielle par session.

### Mécaniques d'engagement

- **Notifications de collaboration** : "Marie a commenté votre carte" → ramène l'utilisateur dans le produit
- **Résumé hebdomadaire** : email récap de l'activité de l'équipe sur ZenithBoard
- **Gamification** : badges d'accomplissement débloqués à chaque milestone (10 boards, 100 cartes, 5 collaborateurs)

## Étape 5 — Monétisation (Freemium → Payant)

### Modèle de monétisation

| Plan | Prix | Limite clé |
|---|---|---|
| Free | 0 € | 3 boards, 2 collaborateurs, 100 Mo stockage |
| Pro | 12 €/user/mois | Boards illimités, 10 collaborateurs, 5 Go, intégrations |
| Business | 24 €/user/mois | Tout illimité, SSO, audit log, support prioritaire |

### Paywall intelligent

Le paywall est déclenché de manière contextuelle lorsque l'utilisateur tente d'accéder à une fonctionnalité premium ou atteint une limite :
- "Vous avez atteint la limite de 3 boards — passez au plan Pro pour continuer à créer"
- L'utilisateur voit un **aperçu** de la feature premium avant de voir le paywall (valeur avant friction)

## Étape 6 — Viralité et expansion

- **Boucle virale native** : inviter des collaborateurs est une action core du produit (pas un extra)
- **K-factor cible** : ≥ 0.4 (chaque utilisateur amène 0.4 nouveaux utilisateurs en moyenne)
- **Expansion** : les équipes qui grandissent ajoutent des sièges automatiquement (billing par siège)

## Métriques clés

| KPI | Cible | Fréquence |
|---|---|---|
| Taux d'activation J7 | ≥ 50 % | Hebdomadaire |
| Taux de conversion Free → Paid | ≥ 5 % | Mensuel |
| K-factor (viralité) | ≥ 0.4 | Mensuel |
| Time-to-Value | < 3 minutes | Hebdomadaire |
| NRR (expansion) | ≥ 120 % | Mensuel |

---

Tags: `PLG`, `product-led-growth`, `funnel`, `freemium`, `viralité`, `activation`, `monétisation`, `self-serve`
