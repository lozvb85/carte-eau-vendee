# L’eau en Vendée — V5 · Alouette

## Projet
Carte web entièrement redessinée, sans reproduction visuelle du document historique Vendée Eau. Fond vectoriel interactif Leaflet + contours des communes API Géo, recherche, barrages cliquables, comparateur et consultation à la demande des résultats du contrôle sanitaire des UDI via Hub'Eau.

## Contenu
- `index.html` : structure de la page.
- `style.css` : charte graphique responsive.
- `script.js` : carte, recherche, fiches, comparaison et API.
- `data.json` : les 13 taux et volumes de remplissage vérifiés au 25 octobre 2026.

## Sources / avertissements
- Vendée Eau, « L’état de la ressource », tableau au **25 octobre 2026**. Les 13 retenues totalisent **18 270 000 m³ stockés**, sur 55 800 000 m³ (32,7 % arrondi par l'exploitant).
- API Découpage administratif : `https://geo.api.gouv.fr/departements/85/communes?format=geojson&geometry=contour`.
- Hub'Eau eau potable : `https://hubeau.eaufrance.fr/api/v1/qualite_eau_potable/`, endpoints `communes_udi` et `resultats_dis`.
- La carte PDF de Vendée Eau de septembre 2020 a servi à documenter les origines, **mais n'est pas le fond graphique de V5**.

### Limites cruciales
1. **Localisation des 13 repères de barrage approximative** : position dérivée du schéma historique, transformée vers la Vendée vectorielle. Elle **n’est pas une géolocalisation officielle**. À remplacer avant publication éditoriale par des coordonnées validées.
2. **Aucune zone barrage→commune n’est inventée** : les zones de distribution d’eau de 2020 ne sont pas des polygones SIG géoréférencés ; leur carte historique est seulement citée.
3. Les chiffres de remplissage décrivent la **quantité d'eau brute**, jamais la qualité sanitaire.
4. Les résultats sanitaires sont chargés à la demande. Si l'API est temporairement indisponible, une erreur est affichée ; aucune mesure n'est créée.
5. Les analyses affichées sont un **extrait de réponse API**, pas un diagnostic global de conformité.
6. Certaines communes peuvent dépendre de plusieurs unités de distribution (UDI).
7. Cette édition utilise des services externes pour la carte vectorielle, les fonds de plan, les polices et les mesures. Elle n'est pas 100 % autonome hors connexion.

## Mettre en ligne gratuitement
1. Décompresser le ZIP.
2. Déposer **les quatre fichiers eux-mêmes**, pas le dossier ni le ZIP, à la racine du dépôt `lozvb85/carte-eau-vendee` sur github.com.
3. Confirmer la présence de `index.html` à la racine.
4. Dans `Settings → Pages` : `Deploy from a branch`, branche `main`, dossier `/(root)`.
5. Ouvrir `https://lozvb85.github.io/carte-eau-vendee/` et forcer le rafraîchissement (Ctrl+F5).

## Pour intégrer dans un article
```html
<iframe title="L'eau en Vendée : carte interactive Alouette" src="https://lozvb85.github.io/carte-eau-vendee/" loading="lazy" style="border:0;width:100%;height:1080px" allowfullscreen></iframe>
```
Pour mobile, prévoir une hauteur initiale d'environ 1400 px, à ajuster sur le site.

## Vérifications
Exécuter `node --check script.js`. Contrôler en situation sur iPhone, Android et desktop : clic, recherche, chargement API, comparaison, redimensionnement, droits d'iframe. **Le rendu navigateur et les API n'ont pas été validés automatiquement dans l'environnement de création.**
