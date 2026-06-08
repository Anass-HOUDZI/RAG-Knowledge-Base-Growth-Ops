# Propriétés de Scoring dans HubSpot

**Tags :** `hubspot`, `lead-scoring`, `scoring`, `MQL`, `SQL`, `growth-ops`
**Dernière mise à jour :** 2026-05-10
**Auteur :** Équipe Growth Ops — ScaleUp Corp

---

## Contexte

Le lead scoring permet de hiérarchiser les contacts selon leur probabilité de conversion. Chez ScaleUp Corp, nous utilisons un modèle de scoring hybride combinant des critères démographiques (fit) et comportementaux (engagement). Ce document détaille la configuration des propriétés de scoring dans HubSpot.

## Architecture du scoring

```
Score Total = Score Fit (démographique) + Score Engagement (comportemental)
             Max 50 pts                    Max 50 pts
             ─────────                     ─────────
             = Score Global sur 100 pts
```

### Seuils de qualification

| Score | Qualification | Action déclenchée |
|-------|--------------|-------------------|
| 0–29 | Froid | Nurturing automatique |
| 30–49 | Tiède | Nurturing avancé |
| 50–69 | MQL | Alerte SDR + assignation |
| 70–89 | SQL | Création deal automatique |
| 90–100 | Hot Lead | Notification manager + appel sous 2h |

## Score Fit — Critères démographiques

### Propriétés HubSpot utilisées

| Propriété | Valeur | Points |
|-----------|--------|--------|
| `company_size` | 50–200 employés | +10 |
| `company_size` | 201–1000 employés | +15 |
| `company_size` | > 1000 employés | +8 |
| `job_title` | Contient "Director", "VP", "Head of" | +15 |
| `job_title` | Contient "Manager" | +10 |
| `job_title` | Contient "Intern", "Student" | -10 |
| `country` | France, Belgique, Suisse | +10 |
| `country` | Autres pays EU | +5 |
| `industry` | SaaS, E-commerce, Fintech | +10 |
| `email_domain` | Gmail, Yahoo, Hotmail (domaines perso) | -15 |

### Configuration dans HubSpot

1. Aller dans **Paramètres > Propriétés > Contacts**
2. Rechercher la propriété `hubspot_score`
3. Cliquer sur **Modifier les critères de scoring**
4. Section **Positif** : ajouter les critères avec les points correspondants
5. Section **Négatif** : ajouter les critères de déduction

> **⚠️ Important :** HubSpot ne permet qu'un seul score natif (`hubspot_score`). Pour le scoring avancé (fit vs. engagement), créer des propriétés calculées personnalisées.

## Score Engagement — Critères comportementaux

| Action | Points | Décroissance |
|--------|--------|-------------|
| Visite page pricing | +15 | -5 après 14j |
| Soumission formulaire demo | +20 | Aucune |
| Ouverture email (par email) | +2 | -1 après 30j |
| Clic email (par clic) | +5 | -2 après 30j |
| Visite blog (par visite) | +1 | -1 après 30j |
| Téléchargement livre blanc | +10 | -3 après 21j |
| Participation webinar | +12 | -4 après 21j |
| Désabonnement email | -20 | Aucune |
| Bounce email | -15 | Aucune |
| Aucune activité > 60j | -25 | Aucune |

### Propriétés personnalisées de scoring

```json
{
  "name": "score_fit",
  "label": "Score Fit (Démographique)",
  "type": "number",
  "fieldType": "number",
  "groupName": "scoring_custom",
  "description": "Score basé sur les critères démographiques du contact"
}
```

```json
{
  "name": "score_engagement",
  "label": "Score Engagement (Comportemental)",
  "type": "number",
  "fieldType": "number",
  "groupName": "scoring_custom",
  "description": "Score basé sur les actions et interactions du contact"
}
```

## Bonnes pratiques

1. **Recalibrer trimestriellement** : Analyser les taux de conversion par tranche de score et ajuster les seuils.
2. **Décroissance temporelle** : Réduire le score engagement des contacts inactifs pour éviter les faux positifs.
3. **Score négatif** : Ne pas hésiter à attribuer des points négatifs (emails personnels, désabonnements).
4. **Alignement Sales-Marketing** : Valider les seuils MQL/SQL avec l'équipe commerciale chaque mois.
5. **Dashboard de suivi** : Créer un rapport de distribution des scores pour détecter les anomalies.

## Pièges courants

- **Score trop généreux** : Trop de MQL = SDR surchargés = perte de confiance dans le scoring
- **Pas de décroissance** : Un contact qui a visité le site il y a 6 mois garde un score élevé artificiellement
- **Ignorer les signaux négatifs** : Les bounces et désabonnements doivent impacter fortement le score

---

*Document interne — ScaleUp Corp Growth Ops*
