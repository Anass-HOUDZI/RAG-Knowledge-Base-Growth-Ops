# Optimisation Conversion Trial → Paid

## Contexte et objectif

Chez **StreamDeck Pro**, le modèle freemium avec trial de 14 jours est le principal moteur d'acquisition. Cependant, le taux de conversion trial → paid stagnait à 8 %, bien en dessous du benchmark SaaS B2B de 15-20 %. L'équipe Growth a lancé un programme d'optimisation systématique visant à porter ce taux à 15 % en 6 mois. Ce playbook documente les leviers identifiés, les expérimentations menées et les processus en place.

## Diagnostic initial

### Analyse du funnel de conversion (cohorte Q4 2024)

| Étape | Taux | Drop-off |
|---|---|---|
| Inscription trial | 100 % | — |
| Setup complété (profil + intégration) | 72 % | 28 % |
| Activation (1ère action core réalisée) | 48 % | 24 % |
| Usage régulier (≥ 3 sessions en semaine 2) | 31 % | 17 % |
| Conversion trial → paid | 8 % | 23 % |

### Causes identifiées

1. **Friction au setup** : trop d'étapes obligatoires avant de voir la valeur
2. **Manque de guidage** : 40 % des utilisateurs trial ne découvrent pas les features clés
3. **Timing de la demande de paiement** : le paywall apparaît à J14 sans préparation progressive
4. **Absence de human touch** : aucune interaction humaine pendant le trial

## Leviers d'optimisation

### Levier 1 — Raccourcir le Time-to-Value

**Actions** :
- Réduire le setup de 7 étapes à 3 étapes (email, mot de passe, première action)
- Proposer des templates pré-configurés au lieu de partir d'un projet vide
- Afficher un tutorial interactif au premier login (3 minutes max)

**Résultat attendu** : +10 points de setup complété

### Levier 2 — Guidage in-app progressif

**Actions** :
- Implémenter une checklist d'onboarding visible dans le dashboard pendant tout le trial
- Afficher des tooltips contextuels sur les features non découvertes
- Envoyer des emails ciblés basés sur les actions NON réalisées (vs réalisées)

**Séquence email trial** :

| Jour | Objet | Condition |
|---|---|---|
| J0 | "Bienvenue — votre checklist pour démarrer" | Tous |
| J2 | "Avez-vous essayé [feature X] ?" | Feature X non utilisée |
| J5 | "Comment [Client fictif] a gagné 5h/semaine" | Tous |
| J8 | "Votre trial est à mi-parcours — voici ce qu'il vous reste à découvrir" | < 50 % checklist complétée |
| J11 | "3 jours restants — sécurisez votre compte" | Tous |
| J13 | "Dernière chance — offre spéciale 20 %" | Non convertis |
| J14 | "Votre trial expire aujourd'hui" | Non convertis |

### Levier 3 — Human touch stratégique

**Actions** :
- Appel de bienvenue automatisé par le SDR à J2 pour les comptes à fort potentiel (ICP score ≥ 70)
- Chat proactif in-app à J7 : "Avez-vous des questions ?"
- Appel de closing par l'AE à J12 pour les comptes activés non convertis

**Critères de priorisation pour l'appel** :
- Taille entreprise ≥ 50 employés
- Utilisation ≥ 5 sessions
- Au moins 1 collaborateur invité

### Levier 4 — Optimisation du paywall

**Actions** :
- Afficher le pricing dès J7 (pas seulement à J14) avec un compteur de valeur générée
- Proposer 3 options de conversion : mensuel, annuel (-20 %), annuel + onboarding (-15 % + 1h offerte)
- Offrir une extension de 7 jours gratuite en échange d'un feedback structuré (pour les hésitants)

## Métriques clés

| KPI | Cible | Fréquence |
|---|---|---|
| Taux de conversion trial → paid | ≥ 15 % | Mensuel |
| Time-to-Value médian | < 2 jours | Hebdomadaire |
| Taux de setup complété | ≥ 85 % | Hebdomadaire |
| Taux d'activation (action core) | ≥ 65 % | Hebdomadaire |
| Revenue per trial (MRR / nombre de trials) | ≥ 12 € | Mensuel |

---

Tags: `trial`, `conversion`, `freemium`, `onboarding`, `paywall`, `time-to-value`, `activation`, `PLG`
