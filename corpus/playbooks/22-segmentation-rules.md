# Règles de Segmentation Clients

## Contexte et objectif

La segmentation est la base de toute communication pertinente chez **ApexSignal**. Une segmentation précise permet de personnaliser les messages, d'optimiser l'allocation des ressources commerciales et de maximiser le ROI des campagnes. Ce playbook définit les segments standards, les règles de classification et les cas d'usage opérationnels pour chaque segment.

## Axes de segmentation

### Axe 1 — Firmographique (B2B)

| Segment | Critère | Volume estimé |
|---|---|---|
| Enterprise | ≥ 500 employés, CA ≥ 50 M€ | 8 % de la base |
| Mid-Market | 50-499 employés, CA 5-50 M€ | 27 % de la base |
| SMB | 10-49 employés, CA 1-5 M€ | 45 % de la base |
| Micro | < 10 employés, CA < 1 M€ | 20 % de la base |

### Axe 2 — Comportemental (engagement produit)

| Segment | Critère | Action |
|---|---|---|
| Power Users | ≥ 5 sessions/semaine, utilisation de 3+ features | Candidats beta, ambassadeurs, expansion |
| Utilisateurs réguliers | 2-4 sessions/semaine | Nurturing valeur, éducation features avancées |
| Utilisateurs occasionnels | < 2 sessions/semaine | Ré-engagement, rappels de valeur |
| Dormants | Aucune session depuis 30+ jours | Campagne de réactivation |
| Churned | Compte annulé | Campagne win-back à 60/90/180 jours |

### Axe 3 — Lifecycle (stade dans le parcours)

| Segment | Stade | Communication type |
|---|---|---|
| Prospects froids | Lead non engagé | Contenu éducatif TOFU |
| Prospects chauds | MQL / SQL | Contenu MOFU + outreach commercial |
| Nouveaux clients (< 90j) | Client récent | Onboarding, adoption, formation |
| Clients matures (90j-1 an) | Client établi | Expansion, QBR, développement de la relation |
| Clients fidèles (> 1 an) | Client long-terme | Programme ambassadeur, beta features, événements exclusifs |

### Axe 4 — Valeur (revenu)

| Segment | Critère | Couverture CS |
|---|---|---|
| Platinum | MRR ≥ 5 000 € | CSM dédié, QBR mensuel |
| Gold | MRR 1 000-4 999 € | CSM partagé (1:20), QBR trimestriel |
| Silver | MRR 200-999 € | Tech-touch uniquement (emails automatisés) |
| Bronze | MRR < 200 € | Self-serve, communauté, documentation |

## Règles de classification

### Priorité des axes

En cas de conflit entre segments, la priorité est :
1. **Valeur** (revenu) → détermine le niveau de service
2. **Comportemental** → détermine les actions opérationnelles
3. **Lifecycle** → détermine le type de contenu
4. **Firmographique** → détermine le potentiel d'expansion

### Règles de mise à jour

- Les segments firmographiques sont mis à jour **trimestriellement** via enrichissement automatique
- Les segments comportementaux sont recalculés **quotidiennement** sur les données d'usage produit
- Les segments lifecycle sont mis à jour **en temps réel** via les workflows CRM
- Les segments valeur sont mis à jour **mensuellement** via synchronisation billing → CRM

### Règles d'exclusion

- Un contact ne peut appartenir qu'à **un seul segment** par axe
- Les contacts sans email valide sont exclus de toute segmentation marketing
- Les employés internes sont exclus de toutes les segmentations (tag `internal_employee`)
- Les concurrents identifiés sont taggés `competitor` et exclus des communications

## Cas d'usage opérationnels

| Cas d'usage | Segments utilisés | Canal |
|---|---|---|
| Campagne upsell Enterprise | Mid-Market + Power Users + Gold | Email personnalisé + appel AE |
| Webinar fonctionnalités avancées | Clients matures + Utilisateurs réguliers | Email invitation |
| Programme de parrainage | Clients fidèles + Power Users + Platinum/Gold | In-app + email |
| Campagne de réactivation | Dormants + Silver/Bronze | Email automatisé |
| Beta test nouvelle feature | Power Users + Clients fidèles | Email exclusif + in-app |

## Métriques clés

| KPI | Cible | Fréquence |
|---|---|---|
| % base correctement segmentée | ≥ 95 % | Mensuel |
| Taux de couverture segmentation (contacts assignés / total) | ≥ 98 % | Mensuel |
| Écart de performance entre segments (taux d'ouverture email) | Documenté | Trimestriel |
| Impact de la personnalisation par segment sur la conversion | ≥ +20 % vs non segmenté | Trimestriel |

---

Tags: `segmentation`, `CRM`, `firmographique`, `comportemental`, `lifecycle`, `personnalisation`, `ciblage`, `clients`
