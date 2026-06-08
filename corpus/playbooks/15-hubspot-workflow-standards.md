# Standards Workflows HubSpot

## Contexte et objectif

Chez **ArcticFlow**, le CRM HubSpot est au cœur des opérations Growth. Avec plus de 85 workflows actifs, la dette technique et les conflits entre workflows sont devenus un risque opérationnel majeur. Ce playbook définit les standards de nommage, de conception, de test et de maintenance des workflows pour garantir leur fiabilité et leur maintenabilité.

## Convention de nommage

Chaque workflow doit suivre le format suivant :

```
[ÉQUIPE] — [TYPE] — [NOM DESCRIPTIF] — [VERSION]
```

**Exemples** :
- `MKT — NURTURE — Séquence découverte TOFU — v2.1`
- `SALES — LIFECYCLE — MQL vers SQL transition — v1.0`
- `OPS — CLEAN — Dédoublonnage contacts hebdo — v1.3`
- `CS — ALERT — Churn risk score élevé — v1.0`

### Codes d'équipe

| Code | Équipe |
|---|---|
| MKT | Marketing |
| SALES | Sales / Revenue |
| OPS | Operations / RevOps |
| CS | Customer Success |
| PROD | Product |

### Codes de type

| Code | Type | Description |
|---|---|---|
| NURTURE | Nurturing | Séquences email de maturation |
| LIFECYCLE | Lifecycle | Transitions de stage du contact |
| ALERT | Alertes | Notifications internes (Slack, email) |
| CLEAN | Nettoyage | Hygiène de données, dédoublonnage |
| ENRICH | Enrichissement | Complétion automatique de propriétés |
| ASSIGN | Assignation | Routage des leads vers les propriétaires |
| SCORE | Scoring | Calcul et mise à jour des scores |
| SYNC | Synchronisation | Sync entre outils (CRM ↔ produit, CRM ↔ billing) |

## Règles de conception

### Principes généraux

1. **Un workflow = un objectif** : ne pas combiner nurturing et scoring dans le même workflow
2. **Critères d'inscription explicites** : toujours documenter le "pourquoi" de chaque critère dans la description du workflow
3. **Branches conditionnelles limitées** : maximum 3 niveaux de profondeur dans les if/then
4. **Délais raisonnables** : pas de délai < 1 heure entre deux actions (risque de spam)
5. **Suppression lists** : toujours exclure les contacts opt-out, les employés internes et les concurrents

### Checklist avant activation

- ☐ Nom conforme à la convention de nommage
- ☐ Description complète (objectif, audience, date de création, auteur)
- ☐ Critères d'inscription vérifiés (pas de critère trop large)
- ☐ Exclusions configurées (opt-out, internes, concurrents)
- ☐ Test sur un échantillon de 5-10 contacts en mode draft
- ☐ Pas de conflit avec un workflow existant (vérifier les propriétés modifiées)
- ☐ Notification de fin de workflow configurée si critique
- ☐ Propriétaire du workflow assigné dans la description

## Gestion des conflits

### Problèmes fréquents

| Conflit | Cause | Solution |
|---|---|---|
| Deux workflows modifient la même propriété | Conditions d'inscription qui se chevauchent | Ajouter des critères d'exclusion mutuels |
| Contact inscrit dans 2 séquences de nurturing | Pas de vérification de l'inscription active | Ajouter une condition "n'est pas actuellement inscrit dans [autre workflow]" |
| Boucle infinie | Un workflow déclenche un changement qui réinscrit dans le même workflow | Ajouter un critère "a déjà été inscrit dans ce workflow" comme exclusion |

### Matrice de priorité

En cas de conflit non résolvable, la priorité suit cet ordre :
1. Workflows LIFECYCLE (transition de stage)
2. Workflows ALERT (notifications critiques)
3. Workflows SCORE (mise à jour des scores)
4. Workflows NURTURE (séquences email)
5. Workflows CLEAN (nettoyage données)

## Maintenance

- **Revue mensuelle** : audit de tous les workflows actifs, désactivation des workflows obsolètes
- **Monitoring hebdomadaire** : vérification des taux d'erreur dans le dashboard workflow
- **Changelog** : toute modification est documentée dans le fichier `Workflows_Changelog` partagé
- **Archivage** : les workflows désactivés depuis plus de 90 jours sont archivés avec la raison de désactivation

## Métriques clés

| KPI | Cible | Fréquence |
|---|---|---|
| Nombre de workflows actifs | < 100 | Mensuel |
| Taux d'erreur workflow (inscriptions échouées) | < 1 % | Hebdomadaire |
| % workflows conformes au nommage | 100 % | Mensuel |
| Temps moyen de résolution conflit | < 24h | Ad hoc |
| % workflows avec description complète | ≥ 95 % | Mensuel |

---

Tags: `HubSpot`, `workflows`, `CRM`, `automation`, `nommage`, `maintenance`, `RevOps`, `standards`
