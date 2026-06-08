# Processus de Handoff Marketing → Sales

## Contexte et objectif

Le handoff entre Marketing et Sales est le point de friction le plus critique du funnel chez **FlowStack**. Un handoff mal exécuté entraîne des leads perdus, des temps de réponse dégradés et une rupture de l'expérience prospect. Ce playbook formalise le processus end-to-end, les SLA et les responsabilités de chaque équipe pour garantir un passage de relais fluide et traçable.

## Définition du point de handoff

Le handoff se déclenche lorsqu'un contact atteint le statut **MQL** (Marketing Qualified Lead) selon les critères définis dans le playbook lead scoring :

- Lead score ≥ 50 (fit + engagement)
- Aucun critère d'exclusion actif (concurrent, étudiant, email personnel)

**Moment précis du handoff** : le contact est transféré à Sales **dans les 4 heures ouvrées** suivant le passage en MQL.

## Processus détaillé

### Étape 1 — Déclenchement automatique (Marketing Ops)

1. Le workflow CRM détecte le passage en MQL
2. **Actions automatiques** :
   - Assignation au SDR selon les règles de routage (round-robin par zone géographique)
   - Notification Slack dans `#new-mqls` avec contexte enrichi :
     ```
     🔔 Nouveau MQL
     Nom : [Prénom Nom]
     Entreprise : [Nom entreprise] — [Secteur]
     Score : [Score total] (Fit: [X] / Engagement: [Y])
     Dernier touchpoint : [Action] — [Date]
     Lien CRM : [URL]
     ```
   - Email de notification au SDR assigné avec les mêmes informations
   - Création d'une tâche CRM "Qualifier le MQL" avec deadline J+1

### Étape 2 — Premier contact (SDR — SLA 24h)

1. Le SDR consulte le profil complet dans le CRM :
   - Historique des interactions marketing (pages visitées, contenus téléchargés, emails ouverts)
   - Firmographiques (taille, secteur, localisation)
   - Score et détail des critères de scoring
2. **Appel de qualification** (15-20 min) structuré autour du framework BANT :
   - Budget : "Avez-vous un budget identifié pour ce type de projet ?"
   - Autorité : "Qui d'autre est impliqué dans cette décision ?"
   - Need : "Quel est le principal défi que vous cherchez à résoudre ?"
   - Timeline : "Avez-vous une échéance en tête pour ce projet ?"
3. **Issue de l'appel** :
   - ✅ Qualifié → passage en SQL, création d'un meeting avec l'AE
   - 🔄 Pas encore prêt → renvoi en nurturing avec tag `recycled_mql`
   - ❌ Non qualifié → passage en "Disqualifié" avec raison documentée

### Étape 3 — Transition vers l'AE (SDR → AE)

1. Le SDR rédige un **briefing de handoff** dans le CRM contenant :
   - Résumé de la conversation de qualification
   - Réponses BANT documentées
   - Objections identifiées
   - Prochaines étapes convenues avec le prospect
   - Participants au meeting côté client
2. Le SDR programme le meeting AE-prospect et envoie l'invitation
3. Le SDR informe l'AE via le canal Slack `#sql-handoff` avec le lien vers le briefing

### Étape 4 — Prise en charge AE

1. L'AE prend connaissance du briefing **avant** le premier meeting
2. L'AE ne repose pas les questions déjà couvertes par le SDR (expérience fluide pour le prospect)
3. Le premier meeting AE est orienté "valeur" et non "requalification"

## SLA et responsabilités

| Étape | Responsable | SLA | Escalade si dépassé |
|---|---|---|---|
| MQL → Assignation SDR | Marketing Ops (auto) | 4h ouvrées | Alerte manager Ops |
| Assignation → Premier contact | SDR | 24h ouvrées | Alerte manager SDR |
| Qualification → Briefing | SDR | 4h après l'appel | N/A |
| Briefing → Meeting AE | SDR | 48h ouvrées | Alerte manager Sales |
| Meeting AE → Suivi prospect | AE | 24h après le meeting | Alerte VP Sales |

## Feedback loop

- **MQL rejeté par Sales** : le SDR documente la raison de rejet dans le CRM → revue hebdomadaire Marketing + Sales pour ajuster les critères de scoring
- **Taux de rejet > 30 %** : déclenchement d'un audit du scoring avec l'équipe Data
- **Feedback SDR** : formulaire mensuel de feedback qualitatif sur la qualité des MQL reçus

## Métriques clés

| KPI | Cible | Fréquence |
|---|---|---|
| Délai moyen MQL → premier contact | < 24h ouvrées | Hebdomadaire |
| Taux d'acceptation MQL (MQL → SQL) | ≥ 25 % | Mensuel |
| Taux de MQL contactés dans le SLA | ≥ 90 % | Hebdomadaire |
| Taux de meeting AE tenu (no-show) | < 15 % | Mensuel |
| Taux de satisfaction SDR sur qualité MQL | ≥ 7/10 | Mensuel |

---

Tags: `handoff`, `MQL`, `SQL`, `SDR`, `AE`, `SLA`, `routing`, `qualification`, `sales-marketing-alignment`
