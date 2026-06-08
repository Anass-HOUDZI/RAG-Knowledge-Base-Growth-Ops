# Bonnes Pratiques Délivrabilité Email

**Tags :** `hubspot`, `email`, `délivrabilité`, `SPF`, `DKIM`, `DMARC`, `growth-ops`
**Dernière mise à jour :** 2026-05-12
**Auteur :** Équipe Growth Ops — ScaleUp Corp

---

## Contexte

La délivrabilité email est un enjeu critique pour ScaleUp Corp. Un email qui n'atteint pas la boîte de réception est un email perdu. Ce guide rassemble les bonnes pratiques pour maintenir un taux de délivrabilité supérieur à 98% et éviter les blacklists.

## Configuration technique

### 1. Authentification DNS

Trois enregistrements DNS sont indispensables pour garantir l'authentification des emails :

| Protocole | Fonction | Enregistrement DNS |
|-----------|----------|-------------------|
| **SPF** | Autorise les serveurs à envoyer au nom du domaine | `v=spf1 include:_spf.hubspot.fictif.com ~all` |
| **DKIM** | Signe cryptographiquement les emails | Clé DKIM générée dans HubSpot > Paramètres Email |
| **DMARC** | Définit la politique en cas d'échec SPF/DKIM | `v=DMARC1; p=quarantine; rua=mailto:dmarc@scaleup-corp.fictif.com` |

### Configuration pas à pas

1. **Paramètres > Domaine et URL > Connecter un domaine d'envoi**
2. Ajouter le domaine `@scaleup-corp.fictif.com`
3. Copier les enregistrements CNAME fournis par HubSpot
4. Les ajouter dans la zone DNS du registrar (ex. : OVH, Cloudflare)
5. Attendre la propagation DNS (jusqu'à 48h)
6. Revenir dans HubSpot et cliquer **Vérifier**

> **⚠️ Important :** Ne pas utiliser `p=none` pour DMARC en production. Passer progressivement de `none` à `quarantine` puis `reject` sur 3 mois.

### 2. Domaine d'envoi dédié

Utiliser un sous-domaine dédié pour les emails marketing :

```
Emails marketing : marketing@news.scaleup-corp.fictif.com
Emails transactionnels : noreply@app.scaleup-corp.fictif.com
Emails commerciaux : prénom@scaleup-corp.fictif.com (domaine principal)
```

Cette séparation protège la réputation du domaine principal en cas de problème de délivrabilité sur les emails marketing.

## Hygiène de la base de contacts

### Nettoyage régulier

| Action | Fréquence | Critère |
|--------|-----------|---------|
| Supprimer les hard bounces | Automatique (workflow) | `email_hard_bounce = true` |
| Identifier les soft bounces récurrents | Hebdomadaire | ≥ 3 soft bounces sur 30 jours |
| Désabonner les inactifs | Mensuelle | Aucune ouverture sur 6 mois ET ≥ 10 emails envoyés |
| Vérifier les emails invalides | À l'import | Utiliser un service de vérification tiers |

### Workflow de nettoyage automatique

```text
Critère d'inscription :
  - Dernier email ouvert > 180 jours
  - Nombre d'emails envoyés ≥ 10
  - lifecyclestage ≠ Customer

Actions :
  1. Envoyer email de réengagement ("Êtes-vous toujours intéressé ?")
  2. Attendre 14 jours
  3. SI aucune ouverture :
     → Mettre email_opt_out = true
     → Ajouter à la liste [STATIC] | EXCL | Inactifs Nettoyés — {date}
```

## Bonnes pratiques de contenu

### Objet de l'email

- **Longueur** : 30–50 caractères (optimal pour mobile)
- **Personnalisation** : Utiliser le prénom `{{contact.firstname}}` pour augmenter le taux d'ouverture de +15%
- **Éviter les spam words** : « GRATUIT », « OFFRE EXCEPTIONNELLE », « CLIQUEZ ICI », « $$$ »
- **A/B testing** : Tester systématiquement 2 objets par campagne (split 50/50)

### Corps de l'email

1. **Ratio texte/image** : Minimum 60% de texte, maximum 40% d'images
2. **Lien de désinscription** : Visible et accessible (obligatoire légalement)
3. **Poids total** : < 100 Ko pour éviter le clipping Gmail
4. **Alt text** : Ajouter un texte alternatif sur toutes les images
5. **Preheader** : Personnaliser le texte de prévisualisation (ne pas laisser par défaut)

## Métriques de délivrabilité

| Métrique | Seuil acceptable | Alerte |
|----------|-----------------|--------|
| Taux de délivrabilité | ≥ 98% | < 95% |
| Taux d'ouverture | ≥ 22% | < 15% |
| Taux de clic | ≥ 3,5% | < 2% |
| Taux de bounce | ≤ 1% | > 2% |
| Taux de plainte spam | ≤ 0,05% | > 0,1% |
| Taux de désinscription | ≤ 0,3% | > 0,5% |

## Actions en cas de dégradation

```text
1. Vérifier les enregistrements DNS (SPF, DKIM, DMARC)
2. Contrôler la réputation du domaine sur mxtoolbox.com
3. Analyser les bounces récents (hard et soft)
4. Réduire temporairement le volume d'envoi
5. Segmenter sur les contacts engagés uniquement
6. Contacter le support HubSpot si blacklist détectée
```

## Pièges courants

- **Acheter des listes** : Jamais. Taux de bounce > 20% garanti, risque de blacklist immédiat.
- **Pas de double opt-in** : En Europe (RGPD), le double opt-in est fortement recommandé.
- **Volume soudain** : Ne jamais passer de 500 à 50 000 emails envoyés d'un coup. Augmenter progressivement (warming).

---

*Document interne — ScaleUp Corp Growth Ops*
