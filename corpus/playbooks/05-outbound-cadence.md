# Cadence d'Outbound Multicanal

## Contexte et objectif

L'équipe SDR de **VortexLabs** opère une cadence outbound structurée sur 21 jours combinant email, LinkedIn et appels téléphoniques. Ce playbook standardise la séquence, les messages et les règles de désengagement pour maximiser le taux de réponse tout en respectant la conformité RGPD. Objectif : atteindre un taux de réponse positive de 8 % et un taux de meeting booké de 4 %.

## Prérequis

- Base de prospection qualifiée (ICP validé, emails vérifiés via outil de vérification)
- Profil LinkedIn SDR optimisé (photo pro, headline orienté valeur, 500+ connexions)
- Outil de séquençage email configuré avec domaine de warm-up dédié
- Base légale RGPD : intérêt légitime documenté pour le B2B

## Structure de la cadence (21 jours)

### Semaine 1 — Ouverture

| Jour | Canal | Action |
|---|---|---|
| J1 | Email | Email #1 — Accroche personnalisée basée sur un trigger (levée de fonds, recrutement, actualité) |
| J2 | LinkedIn | Visite du profil + like d'un post récent |
| J3 | LinkedIn | Demande de connexion avec note personnalisée (max 300 caractères) |
| J5 | Email | Email #2 — Relance avec valeur ajoutée (étude de cas sectorielle) |

### Semaine 2 — Intensification

| Jour | Canal | Action |
|---|---|---|
| J8 | Téléphone | Appel #1 — Script court (30 sec max), laisser un message vocal si non réponse |
| J9 | Email | Email #3 — Angle différent (témoignage client ou donnée marché) |
| J11 | LinkedIn | Message InMail ou message direct si connexion acceptée |
| J12 | Téléphone | Appel #2 — Tenter un créneau différent (matin vs après-midi) |

### Semaine 3 — Clôture

| Jour | Canal | Action |
|---|---|---|
| J15 | Email | Email #4 — "Breakup email" annonçant la fin de la séquence |
| J18 | LinkedIn | Dernier message — partage d'une ressource utile sans demande |
| J21 | — | Fin de séquence — passage en statut "Nurture" ou "Disqualifié" |

## Templates email

### Email #1 — Accroche trigger

```
Objet : [Prénom], question rapide sur [trigger identifié]

Bonjour [Prénom],

J'ai vu que [entreprise] venait de [trigger : recruter 5 devs / lever 10M€ / lancer un nouveau produit]. 
Félicitations !

Chez VortexLabs, on accompagne des entreprises comme [exemple client similaire] 
à [bénéfice clé] — résultat : [métrique : +40 % de productivité en 3 mois].

Auriez-vous 15 minutes cette semaine pour en discuter ?

[Signature]
```

### Email #4 — Breakup

```
Objet : Je ferme votre dossier

Bonjour [Prénom],

Je vous ai contacté(e) plusieurs fois sans réponse — je ne veux surtout 
pas être intrusif. Je ferme votre dossier de mon côté.

Si le sujet [problème adressé] redevient prioritaire, n'hésitez pas à 
me recontacter — je serai disponible.

Bonne continuation,
[Signature]
```

## Règles de désengagement

- **Réponse négative** : arrêt immédiat, ajout en liste "Do Not Contact" pour 6 mois
- **Demande RGPD** : suppression des données sous 72h, documentation dans le registre
- **Out of Office** : reprogrammer la séquence à la date de retour + 2 jours
- **Réponse positive** : arrêt de la séquence, handoff vers l'AE

## Métriques clés

| KPI | Cible | Fréquence |
|---|---|---|
| Taux d'ouverture email | ≥ 45 % | Hebdomadaire |
| Taux de réponse (tous canaux) | ≥ 12 % | Hebdomadaire |
| Taux de réponse positive | ≥ 8 % | Hebdomadaire |
| Taux de meeting booké | ≥ 4 % | Hebdomadaire |
| Connexions LinkedIn acceptées | ≥ 30 % | Hebdomadaire |
| Volume prospects contactés / SDR / semaine | 50-80 | Hebdomadaire |

---

Tags: `outbound`, `cadence`, `SDR`, `prospection`, `multicanal`, `email`, `LinkedIn`, `cold-calling`, `RGPD`
