# Framework d'Expérimentation Pricing

## Contexte et objectif

Le pricing est le levier de croissance le plus sous-exploité chez la plupart des SaaS. Chez **QuantumSale**, l'équipe Growth a mis en place un framework rigoureux pour tester et optimiser la stratégie de pricing sans mettre en péril le revenu existant. Ce playbook formalise la méthodologie, les garde-fous et les processus de décision.

## Principes fondamentaux

1. **Ne jamais tester le prix sur les clients existants** — les expérimentations pricing se font uniquement sur les nouveaux visiteurs ou les prospects en phase de considération
2. **Tester la valeur perçue, pas seulement le chiffre** — le prix n'est qu'un symptôme de la perception de valeur
3. **Documenter chaque test** — hypothèse, design, résultats, décision
4. **Durée minimale de test** : 4 semaines ou 500 visiteurs par variante (selon ce qui arrive en dernier)

## Types d'expérimentation

### 1. Test de la page pricing (A/B test)

**Objectif** : optimiser la présentation des plans pour maximiser le taux de conversion page pricing → souscription.

Variables testables :
- Nombre de plans affichés (3 vs 4)
- Plan mis en avant (highlight du plan recommandé)
- Affichage mensuel vs annuel par défaut
- Ancrage de prix (affichage du plan Enterprise pour valoriser le plan Pro)
- Formulation de la valeur (features vs bénéfices)

**Exemple de test réalisé :**

| Variante | Description | Conversion | Résultat |
|---|---|---|---|
| Contrôle | 3 plans, prix mensuel affiché, plan Pro en highlight | 3,2 % | Baseline |
| Variante A | 3 plans, prix annuel affiché (économie mise en avant) | 3,8 % | +18,7 % ✅ |
| Variante B | 4 plans (ajout d'un plan Enterprise), prix mensuel | 2,9 % | -9,4 % ❌ |

### 2. Test de seuil de prix (Van Westendorp)

**Objectif** : déterminer la fourchette de prix acceptable pour un segment donné.

Méthodologie :
1. Sélectionner un panel de 150-200 prospects qualifiés
2. Poser les 4 questions Van Westendorp :
   - À quel prix ce produit vous semble trop cher ?
   - À quel prix ce produit vous semble cher mais acceptable ?
   - À quel prix ce produit vous semble bon marché ?
   - À quel prix ce produit vous semble trop bon marché (qualité douteuse) ?
3. Tracer les courbes et identifier le Point de Prix Optimal (OPP) et la fourchette acceptable

### 3. Test de packaging (feature gating)

**Objectif** : identifier quelles fonctionnalités doivent être dans quel plan pour maximiser l'upgrade.

Approche :
1. Lister les 20 fonctionnalités du produit
2. Classer chaque fonctionnalité en MaxDiff (importance relative perçue par les utilisateurs)
3. Identifier les features "gates" : celles qui motivent l'upgrade sans frustrer la rétention du plan gratuit

| Catégorie | Critère | Placement |
|---|---|---|
| Feature core | Indispensable pour l'activation | Plan gratuit |
| Feature gate | Haute valeur perçue, non indispensable | Plan Pro |
| Feature premium | Différenciante, niche | Plan Enterprise |
| Feature commodity | Faible différenciation | Tous les plans |

## Garde-fous

- **Pas de test simultané** sur la page pricing : un seul test actif à la fois
- **Isolation du trafic** : les utilisateurs exposés à un test pricing ne sont pas exposés à d'autres tests UX
- **Monitoring revenu** : alerte automatique si le MRR des nouveaux clients baisse de plus de 10 % sur 7 jours
- **Validation juridique** : tout changement de pricing public doit être validé par le département légal

## Métriques clés

| KPI | Cible | Fréquence |
|---|---|---|
| Taux de conversion page pricing → souscription | ≥ 3,5 % | Par test |
| ARPU (Average Revenue Per User) | Croissance ≥ 5 % / trimestre | Trimestriel |
| Mix plan (% Pro vs Enterprise) | Cible : 60 % Pro, 25 % Enterprise | Mensuel |
| LTV / CAC ratio | ≥ 3:1 | Trimestriel |
| Élasticité prix estimée | Mesurée par test | Par test |

---

Tags: `pricing`, `expérimentation`, `A/B-test`, `Van-Westendorp`, `packaging`, `ARPU`, `conversion`, `monétisation`
