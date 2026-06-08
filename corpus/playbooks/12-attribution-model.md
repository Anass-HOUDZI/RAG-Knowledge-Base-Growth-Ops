# Modèle d'Attribution Multi-Touch

## Contexte et objectif

Comprendre quels canaux et quels touchpoints contribuent réellement à la conversion est essentiel pour allouer le budget marketing de manière optimale. Chez **PulsarMetrics**, l'équipe Growth Ops a implémenté un modèle d'attribution multi-touch pour remplacer l'attribution last-click, jugée trop biaisée en faveur des canaux de conversion directe. Ce playbook décrit les modèles disponibles, la configuration technique et les règles d'interprétation.

## Limites de l'attribution last-click

L'attribution last-click attribue 100 % du crédit au dernier touchpoint avant la conversion. Problèmes identifiés chez PulsarMetrics :

- Le SEO et le contenu blog (top of funnel) recevaient 0 % du crédit alors qu'ils initiaient 45 % des parcours
- Les campagnes de retargeting (last touch fréquent) recevaient un crédit disproportionné
- Les décisions budgétaires étaient biaisées : sur-investissement retargeting, sous-investissement contenu

## Modèles d'attribution disponibles

| Modèle | Description | Cas d'usage |
|---|---|---|
| **First-touch** | 100 % du crédit au premier touchpoint | Évaluer les canaux de découverte |
| **Last-touch** | 100 % du crédit au dernier touchpoint | Évaluer les canaux de conversion |
| **Linéaire** | Crédit réparti également entre tous les touchpoints | Vue équilibrée, baseline |
| **Time-decay** | Plus de crédit aux touchpoints proches de la conversion | Favorise les canaux d'accélération |
| **Position-based (U-shape)** | 40 % premier, 40 % dernier, 20 % répartis au milieu | Modèle recommandé par défaut |
| **Data-driven (Markov)** | Crédit basé sur la probabilité de conversion de chaque canal | Modèle avancé si données suffisantes |

## Modèle retenu : Position-Based (U-Shape)

Après analyse comparative sur 6 mois de données (2 300 conversions), le modèle Position-Based a été retenu comme modèle principal :

```
Touchpoint 1 (First-touch)   →  40 % du crédit
Touchpoints intermédiaires    →  20 % répartis équitablement
Touchpoint N (Last-touch)     →  40 % du crédit
```

**Justification** : ce modèle valorise à la fois l'acquisition initiale et la conversion finale, tout en reconnaissant le rôle du nurturing intermédiaire.

## Configuration technique

### Sources de données

1. **Web analytics** : tracking UTM systématique sur tous les liens marketing
2. **CRM** : enregistrement de chaque touchpoint dans la timeline contact
3. **Advertising** : import automatique des données de coût par plateforme publicitaire
4. **Produit** : événements in-app trackés et associés au contact CRM

### Convention UTM

```
utm_source   = plateforme (google, linkedin, newsletter, partner)
utm_medium   = type de média (cpc, organic, email, social, referral)
utm_campaign = nom de campagne (format : YYYY-MM_nom-campagne)
utm_content  = variante créative (ad-v1, cta-banner, blog-footer)
utm_term     = mot-clé (pour les campagnes search uniquement)
```

### Fenêtre d'attribution

- **Fenêtre lookback** : 90 jours avant la conversion
- **Touchpoints minimum** : 1 (les conversions direct sont attribuées au first-touch connu le plus récent)
- **Touchpoints maximum comptabilisés** : 15 (au-delà, les plus anciens sont regroupés en "Other")

## Exemple d'attribution sur un deal

**Deal converti** : TechVenture SA — 24 000 € ACV

| # | Date | Touchpoint | Canal | Crédit (U-Shape) |
|---|---|---|---|---|
| 1 | 15 jan | Article blog SEO | Organic | 40 % = 9 600 € |
| 2 | 22 jan | Téléchargement ebook | Email nurturing | 6,7 % = 1 600 € |
| 3 | 3 fév | Webinar | Social (LinkedIn) | 6,7 % = 1 600 € |
| 4 | 18 fév | Retargeting ad | Paid (Display) | 6,7 % = 1 600 € |
| 5 | 2 mar | Demande de démo | Direct / CPC | 40 % = 9 600 € |

## Règles d'interprétation

- **Ne jamais comparer attribution single-touch et multi-touch** directement — les métriques ne sont pas compatibles
- **Analyser les tendances** plutôt que les valeurs absolues — un canal qui croît en attribution relative mérite plus d'investissement
- **Croiser avec le coût par canal** pour calculer le ROI attribué par canal
- **Revoir le modèle tous les 6 mois** ou après un changement majeur de mix canal

## Métriques clés

| KPI | Cible | Fréquence |
|---|---|---|
| Couverture d'attribution (% deals avec tracking complet) | ≥ 85 % | Mensuel |
| Nombre moyen de touchpoints par conversion | 4-6 | Mensuel |
| ROI par canal (revenue attribué / coût) | ≥ 3:1 sur les canaux majeurs | Trimestriel |
| Écart attribution U-shape vs last-click par canal | Documenté | Trimestriel |

---

Tags: `attribution`, `multi-touch`, `UTM`, `ROI`, `marketing-analytics`, `position-based`, `data-driven`, `budget-allocation`
