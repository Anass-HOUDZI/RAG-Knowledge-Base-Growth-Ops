# Growth Accounting

## Contexte
Le Growth Accounting (comptabilité de croissance) est le cadre analytique de référence chez GrowthFlow SaaS pour décomposer et comprendre les variations de notre base d'utilisateurs actifs et de notre revenu (MRR) d'un mois sur l'autre.

## Les Composantes du Growth Accounting

Pour un mois donné (ex: Mai), nous classons nos utilisateurs/revenus dans ces 4 catégories exclusives :

1.  **Nouveau (New) :** Utilisateurs qui se sont inscrits pour la première fois en Mai. C'est l'indicateur d'efficacité de l'Acquisition.
2.  **Retenu (Retained) :** Utilisateurs qui étaient actifs en Avril ET qui sont restés actifs en Mai. C'est l'indicateur clé de la Rétention pure.
3.  **Ressuscité (Resurrected) :** Utilisateurs qui étaient inactifs en Avril (ou avant), mais qui sont redevenus actifs en Mai. C'est l'indicateur d'efficacité de nos campagnes de Réactivation.
4.  **Churné (Churned) :** Utilisateurs qui étaient actifs en Avril, mais qui sont devenus inactifs (ou ont résilié) en Mai.

*La somme (Nouveau + Retenu + Ressuscité) correspond au nombre total d'utilisateurs actifs en Mai.*

## L'Équation de Croissance

Pour évaluer la santé de notre croissance nette, nous utilisons cette formule simple :
**Croissance Nette (Net Growth) = (Nouveau + Ressuscité) - Churné**

*   Si la Croissance Nette est positive : L'entreprise grandit, l'acquisition compense la perte.
*   Si la Croissance Nette est négative : Le produit perd des utilisateurs plus vite qu'il n'en gagne (Leaky Bucket effect).

## Le Quick Ratio

Le Quick Ratio est une métrique dérivée essentielle que nous suivons chaque mois au niveau Exec :
**Quick Ratio = (Nouveau + Ressuscité) / Churné**

*   **Quick Ratio < 1 :** Déclin (grave problème de rétention).
*   **Quick Ratio de 1 à 2 :** Croissance faible, forte dépendance à l'acquisition.
*   **Quick Ratio > 4 :** Croissance très saine, caractéristique des meilleures entreprises SaaS.

## Processus d'Analyse Mensuelle
1.  Le 2 de chaque mois, l'équipe Data génère le dashboard Growth Accounting (voir modèle `mart_growth_accounting`).
2.  Le Growth Lead analyse les variations suspectes (ex: pic de churn, baisse des ressuscités).
3.  Présentation des résultats lors du meeting All-Hands mensuel.

## Métriques Complémentaires
*   Expansion Revenue (Up-sell / Cross-sell des utilisateurs retenus)
*   Contraction Revenue (Down-sell des utilisateurs retenus)

Tags: metrics, growth-accounting, analytics, retention, churn, quick-ratio
