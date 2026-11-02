# Carte interactive – origines principales de l'eau potable en Vendée

## Périmètre et limites

Première version interactive basée **strictement sur la carte Vendée Eau / CPA (septembre 2020)** fournie par l'utilisateur : `carte11_origines-de-leau.pdf`.

**Important :** le document donne une représentation schématique de réseaux, captages, usines et zones d'origines principales en 2020. Il ne contient ni les taux de remplissage individuels des 13 barrages, ni les concentrations mesurées, ni une table des correspondances actuelles entre barrages et communes. Il serait trompeur de créer ces chiffres à partir du PDF ou d'affirmer qu'une commune reçoit aujourd'hui exclusivement l'eau d'un barrage. Les points interactifs sont placés manuellement sur les pictogrammes du document ; leurs positions ne sont pas des coordonnées GPS. Ils sont identifiés comme **usine** ou **captage** et non présumés être les 13 barrages.

## Pour publier sur GitHub Pages

1. Téléchargez le ZIP et extrayez-le.
2. Dans le dépôt `carte-eau-vendee`, ouvrez **Add file → Upload files**.
3. Placez **directement à la racine** `index.html`, `fond-origines.webp` et `README.md` (pas de sous-dossier). Remplacez les fichiers si demandé.
4. Cliquez sur **Commit changes**.
5. Vérifiez **Settings → Pages → Build and deployment → Deploy from a branch → main → /(root)**.
6. Ouvrez `https://lozvb85.github.io/carte-eau-vendee/` et actualisez avec Ctrl+F5.

La carte nécessite Internet pour la bibliothèque gratuite Leaflet (CDN), mais l'image cartographique est stockée localement : pas d'appel à une API de données et pas de clé payante.

## Code iframe

```html
<iframe src="https://lozvb85.github.io/carte-eau-vendee/" title="Origines de l'eau potable en Vendée — carte historique interactive" loading="lazy" style="width:100%;height:1050px;border:0" referrerpolicy="no-referrer"></iframe>
```

Sur mobile, prévoir environ 1400 px. Ajuster en fonction de la largeur du site. Les pages et l'iframe sont volontairement conçues pour laisser défiler l'article verticalement.

## Suite des investigations

Données nécessaires pour produire la carte finale :
- Barrages : localisation géographique officielle de chacun des 13 ouvrages, taux de remplissage datés **par barrage**, et méthode de calcul.
- Zones : limites SIG des UDI et correspondances effectives usine → réseau → commune, en précisant les interconnexions et transferts.
- Qualité : résultats historiques d'analyses sur eau brute **distincts** de ceux sur l'eau traitée / distribuée, avec dates, valeurs, unités, seuils et restrictions le cas échéant.

Ne pas publier les secteurs 2020 comme état actuel sans une vérification auprès de Vendée Eau.
