# Séquences de Nurturing Email

## Contexte et objectif

Chez **SynapseHub**, les leads qui ne sont pas immédiatement prêts à acheter représentent 75 % du volume entrant. L'équipe Growth a conçu un système de nurturing email segmenté pour maintenir l'engagement de ces leads et les faire progresser dans le funnel. Ce playbook couvre les 4 séquences principales, les règles de segmentation et les critères de sortie.

## Architecture des séquences

```
Lead entrant
    │
    ├── Séquence A : Découverte (TOFU)
    │       └── Sortie → Séquence B ou MQL
    │
    ├── Séquence B : Considération (MOFU)
    │       └── Sortie → MQL ou SQL
    │
    ├── Séquence C : Re-engagement (Inactifs)
    │       └── Sortie → Séquence A/B ou Désabonnement
    │
    └── Séquence D : Post-démo (sans conversion)
            └── Sortie → SQL ou Nurture long-terme
```

## Séquence A — Découverte (TOFU)

**Audience** : Leads ayant téléchargé un contenu éducatif ou s'étant inscrits à la newsletter.
**Durée** : 28 jours, 5 emails.

| Email | Jour | Objet | Contenu | CTA |
|---|---|---|---|---|
| A1 | J0 | Bienvenue + ressource promise | Livraison du contenu + introduction de SynapseHub | Lire le guide |
| A2 | J5 | Article blog complémentaire | Contenu éducatif lié au sujet du téléchargement | Lire l'article |
| A3 | J12 | Étude de cas sectorielle | Résultats concrets d'un client fictif du même secteur | Voir l'étude |
| A4 | J20 | Webinar replay ou vidéo démo | Contenu vidéo de 5 min montrant le produit | Regarder |
| A5 | J28 | Invitation à réserver une démo | Proposition directe + preuve sociale | Réserver |

**Critère de sortie** : clic sur CTA démo (A5) → bascule en MQL. Score ≥ 50 → sortie anticipée.

## Séquence B — Considération (MOFU)

**Audience** : MQL ayant montré un intérêt mais n'ayant pas encore demandé de démo.
**Durée** : 21 jours, 4 emails.

| Email | Jour | Objet | Contenu |
|---|---|---|---|
| B1 | J0 | Comparatif : nous vs alternatives | Tableau comparatif objectif (sans nommer de concurrents réels) |
| B2 | J7 | ROI Calculator | Lien vers le calculateur de ROI interactif |
| B3 | J14 | Témoignage vidéo client | Interview de 3 min avec un champion client |
| B4 | J21 | Offre limitée d'essai | 14 jours d'essai gratuit avec onboarding personnalisé |

## Séquence C — Re-engagement

**Audience** : Leads inactifs depuis 60+ jours (aucune ouverture email, aucune visite site).
**Durée** : 14 jours, 3 emails.

| Email | Jour | Objet |
|---|---|---|
| C1 | J0 | "On ne vous a pas oublié" — nouveautés produit des 3 derniers mois |
| C2 | J7 | Contenu à forte valeur (benchmark sectoriel exclusif) |
| C3 | J14 | "Souhaitez-vous rester abonné(e) ?" — email de confirmation opt-in |

**Règle** : aucune interaction après C3 → suppression de la liste active (hygiène de base).

## Séquence D — Post-démo sans conversion

**Audience** : Leads ayant eu une démo mais n'ayant pas converti dans les 14 jours suivants.
**Durée** : 30 jours, 4 emails.

| Email | Jour | Contenu |
|---|---|---|
| D1 | J0 | Récapitulatif personnalisé de la démo + réponses aux objections identifiées |
| D2 | J10 | Cas d'usage avancé pertinent pour leur contexte |
| D3 | J20 | Invitation à un workshop technique gratuit |
| D4 | J30 | Breakup email — "On reste disponibles quand vous serez prêt(e)" |

## Règles transversales

- **Fréquence maximale** : un lead ne reçoit jamais plus de 2 emails de nurturing par semaine (toutes séquences confondues)
- **Exclusions** : les clients actifs, les opportunités ouvertes et les contacts désabonnés sont exclus de toutes les séquences
- **Personnalisation** : chaque email utilise le prénom, le secteur et le dernier contenu consulté
- **A/B testing** : les objets sont systématiquement testés en A/B sur les 20 % premiers envois

## Métriques clés

| KPI | Cible | Fréquence |
|---|---|---|
| Taux d'ouverture moyen (toutes séquences) | ≥ 35 % | Mensuel |
| Taux de clic moyen | ≥ 8 % | Mensuel |
| Taux de désabonnement | < 0,5 % par email | Mensuel |
| Taux de conversion séquence → MQL | ≥ 15 % | Mensuel |
| Taux de conversion séquence → démo | ≥ 5 % | Mensuel |

---

Tags: `nurturing`, `email-marketing`, `séquence`, `TOFU`, `MOFU`, `re-engagement`, `automation`, `lead-management`
