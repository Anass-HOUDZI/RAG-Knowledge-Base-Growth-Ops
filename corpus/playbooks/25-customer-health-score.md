# Calcul du Customer Health Score

## Contexte
Le Customer Health Score (CHS) est une métrique composite permettant d'évaluer la "santé" d'un client et de prédire son risque de churn ou son potentiel d'upsell. Ce playbook détaille comment nous calculons et utilisons cette métrique chez ScaleUp Corp.

## Composantes du Score

Notre modèle de CHS sur 100 points repose sur 4 piliers :

1.  **Utilisation du Produit (Product Usage) - 40 points**
    *   Fréquence de connexion (WAU/MAU)
    *   Utilisation des fonctionnalités "Core" (ex: export de rapports)
    *   Adoption de nouvelles fonctionnalités
2.  **Support et Engagement (Support & Engagement) - 20 points**
    *   Volume de tickets support ouverts (trop = risque, zéro = désengagement)
    *   Temps de résolution des tickets
    *   Participation aux webinaires / consultation de la documentation
3.  **Satisfaction Client (Customer Satisfaction) - 20 points**
    *   NPS (Net Promoter Score) récent
    *   CSAT (Customer Satisfaction Score) suite aux interactions support
4.  **Santé Financière (Financial Health) - 20 points**
    *   Retards de paiement
    *   Taux de consommation des crédits/licences par rapport au contrat

## Catégorisation et Actions

Le score global détermine la catégorie de santé du client et déclenche des playbooks spécifiques :

*   **Sain (Healthy) : 80 - 100**
    *   Action : Campagnes d'advocacy (demande d'avis, cas client).
    *   Action : Identification d'opportunités d'upsell/cross-sell (expansion revenue).
*   **Alerte (At Risk) : 50 - 79**
    *   Action : Revue de compte trimestrielle (QBR) proactive par le CSM.
    *   Action : Séquence d'email ciblée sur l'adoption des features non utilisées.
*   **Critique (Critical) : < 50**
    *   Action : Alerte immédiate au CSM et au Head of Customer Success.
    *   Action : Appel de "sauvetage" planifié dans les 48h.
    *   Action : Suspension temporaire des campagnes marketing promotionnelles.

## Métriques clés à suivre
*   Score moyen du portfolio client
*   Évolution du CHS sur les 30 derniers jours (Trend)
*   Corrélation entre le CHS et le taux de churn effectif

Tags: health-score, customer-success, churn-prevention, metrics, scoring
