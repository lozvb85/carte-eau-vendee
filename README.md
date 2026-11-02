# Carte de l'eau en Vendée — prototype de travail (Alouette)

**Statut : NON VALIDÉ POUR PUBLICATION JOURNALISTIQUE.** La carte communale, la recherche, les appels Hub'Eau, les fiches et le volet barrages sont implémentés. Les 13 positions exactes, leurs remplissages individuels et leurs zones de desserte ne sont PAS documentés par un jeu de données validé dans ce paquet. Ne pas présenter cette version comme une cartographie exhaustive des ouvrages.

## Fichiers
- `index.html` : page complète ;
- `style.css` : design responsive ;
- `script.js` : carte Leaflet, recherche commune, requêtes Hub'Eau, liste d'ouvrages, comparaison sans donnée inventée.

## Sources officielles
- Vendée Eau, taux global des retenues **32,7 % au 25 octobre 2026** : https://www.vendee-eau.fr/letat-de-la-ressource/
- Vendée Eau, interconnexions et ressources : https://www.vendee-eau.fr/l-eau-une-ressource-limitee/
- Ministère chargé de la Santé / base SISE-Eaux : https://www.data.gouv.fr/datasets/resultats-du-controle-sanitaire-de-leau-distribuee-commune-par-commune
- Hub'Eau qualité eau potable : https://www.data.gouv.fr/dataservices/hubeau-qualite-de-leau-potable
- API Géo limites communes : https://geo.api.gouv.fr/
- Fiche ARS 2025 « Réservoirs Frétière Beaulieu » transmise par la rédaction.

**Important** : la liste de treize noms du script recense des retenues, ouvrages de complexes et/ou usines mentionnés dans des publications anciennes. Elle n'est **pas** une liste officielle certifiée des 13 barrages annoncés par Vendée Eau. Le complexe de Mervent comprend notamment plusieurs ouvrages. Aucun lien barrage → réseau → commune n'est supposé. Les noms et les positions doivent être validés avant diffusion.

## Installation GitHub Pages
1. Décompresser l'archive ZIP.
2. Sur `github.com/lozvb85/carte-eau-vendee`, onglet **Code**, bouton **Add file > Upload files**.
3. Déposer **les fichiers** `index.html`, `style.css`, `script.js`, `README.md` à la racine (pas le dossier ni le ZIP).
4. Valider via **Commit changes** (écraser les fichiers portant le même nom si nécessaire).
5. **Settings > Pages > Deploy from a branch**, choisir `main` et `/(root)`, puis **Save**.
6. Tester `https://lozvb85.github.io/carte-eau-vendee/`.

## Iframe
```html
<iframe src="https://lozvb85.github.io/carte-eau-vendee/" title="L'eau du robinet en Vendée" loading="lazy" style="width:100%;height:2200px;border:0" referrerpolicy="strict-origin-when-cross-origin"></iframe>
```
Sur mobile, prévoir environ 3000 px ou utiliser un iframe à hauteur dynamique si le CMS l'autorise.

## Avant toute publication
- Récupérer le tableau des 13 barrages avec **codes d'ouvrages, coordonnées vérifiées, remplissages individuels et dates**, auprès de Vendée Eau.
- Récupérer les polygones des **zones effectivement desservies** par barrage/usine et les correspondances UDI, qui changent avec les interconnexions. Ne pas dessiner des zones fictives.
- Récupérer les **analyses d'eau brute** par site et les analyses **d'eau distribuée** par UDI ; ne pas les confondre.
- Contrôler l'API Hub'Eau et son schéma à l'exécution ; le prototype peut montrer des erreurs de récupération, sans afficher de conclusion sanitaire.
- Tester physiquement Safari iOS, Chrome Android, et à 320, 375, 390, 430, 768 et 1440 px.

## Tests réalisés
- Présence des fichiers dans l'archive, syntaxe JavaScript (si Node disponible), compatibilité statique GitHub Pages.
- **Non réalisés** : validation visuelle navigateur, résultats live des APIs, positions des barrages, remplissages par barrage, desserte des communes, tests appareils.
