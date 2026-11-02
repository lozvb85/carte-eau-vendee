# L'eau en Vendée — carte interactive V3

Prototype éditorial autonome pour GitHub Pages. Les 13 barrages et les pourcentages proviennent du tableau « Niveaux et volumes stockés dans les retenues », situation au **25 octobre 2026** (PDF fourni : `jspdf-generate (1).pdf`, page 1, Vendée Eau).

La carte de fond est une reproduction du document **« Origines principales de l'eau potable en Vendée »**, Vendée Eau / CPA, septembre 2020 (PDF fourni par l'utilisatrice). Les secteurs d'alimentation colorés reflètent **2020**, pas nécessairement la répartition actuelle. Certains repères sont volontairement notés approximatifs : l'image est un schéma, pas un fond géoréférencé.

Le tableau fait état de 13 retenues, de 18,27 millions de m³ stockés sur un maximum de 55,8 millions, soit 32,7 % au total (source originale).

## Publication

Dans https://github.com/lozvb85/carte-eau-vendee : `Add file > Upload files`. Glisser **les cinq fichiers situés à la racine du dossier décompressé** : `index.html`, `style.css`, `script.js`, `data.json`, `fond-origines.webp`. Ne pas envoyer le ZIP, ni un dossier parent. Cliquer `Commit changes`.

Dans `Settings > Pages`, sélectionner `Deploy from a branch`, `main`, `/(root)`, `Save`. Après publication : https://lozvb85.github.io/carte-eau-vendee/

Pour intégration Alouette (à adapter selon CMS) :

```html
<iframe src="https://lozvb85.github.io/carte-eau-vendee/" title="Les barrages de Vendée et leurs taux de remplissage" width="100%" height="1300" loading="lazy" style="width:100%;border:0"></iframe>
```

Hauteur indicative : 1300 px sur ordinateur, 1800–2100 px sur mobile. Tester avec le CMS et ajuster.

## Portée éditoriale

- Couleur des **points** : remplissage du barrage le 25 octobre 2026 ; elle ne renseigne pas la qualité sanitaire de l'eau.
- Couleur des **secteurs du fond** : origine principale d'approvisionnement en 2020, sans lien avec une note de qualité.
- Interconnexions schématiques et historiques ; ne pas présenter ces secteurs comme des zones de distribution exclusives ou les trajets permanents d'une molécule.
- Aucune analyse sanitaire par barrage ni commune dans ces données. **Ne pas publier des conclusions sur la potabilité à partir du remplissage**.
- Niveaux et volumes sont reproduits du tableau source et peuvent différer légèrement lors du calcul `stocké/capacité` du fait des arrondis du fournisseur.

## Tests

`node --check script.js` et contrôle du JSON exécutés. Les essais navigateur complets doivent encore être effectués notamment sur Safari iOS et Android. Pas de géoréférencement officialisé des marqueurs. La carte est une base graphique opérationnelle et non une datavisualisation complète de qualité de l'eau potable.
