# L'eau du robinet en Vendée — prototype Alouette

## Installation
Décompresser les fichiers et déposer `index.html`, `style.css`, `script.js` à la racine d’un dépôt GitHub public. Dans **Settings → Pages**, choisir **Deploy from a branch**, `main`, `/(root)`. Accéder à `https://PSEUDO.github.io/NOM-DU-DEPOT/`.

## Statut : prototype non validé pour publication rédactionnelle
**Ce prototype n'est pas un bilan exhaustif des contrôles sanitaires et ne permet pas d'affirmer que l'eau d'une commune est conforme.** Aucun chiffre de laboratoire n'est simulé. Les contours sont chargés par l'API Géo, et les correspondances et analyses recherchées au moment du clic par l'API Hub'Eau. La disponibilité et le contrat exact de ces API doivent être vérifiés en navigateur réel. Pas de géométries ni de données d'analyse préchargées, donc le fonctionnement hors ligne n'est pas garanti.

### Sources
- https://www.data.gouv.fr/datasets/resultats-du-controle-sanitaire-de-leau-distribuee-commune-par-commune (PLV, RESULT, UDI_COM)
- https://www.data.gouv.fr/dataservices/hubeau-qualite-de-leau-potable
- https://geo.api.gouv.fr/
- https://www.vendee-eau.fr/l-eau-une-ressource-limitee/

### Prudence d'interprétation
Une commune peut être raccordée à plusieurs UDI. Des prélèvements peuvent être effectués en amont. Seule une comparaison paramètre par paramètre avec les valeurs applicables, dates de validité et conclusions de l'ARS permet une présentation sanitaire. L'API peut paginer les résultats : une seule page n'est pas un contrôle exhaustif. Les 13 barrages sont mentionnés à titre de contexte, sans localisation inventée ni lien présumé avec une commune.

### Cas ARS 2025 « Réservoirs Frétière Beaulieu »
Fiche photographiée par l'utilisatrice, éditée le 12/05/2026 : note C pour bromates (maximum 14 µg/L contre limite 10 µg/L ; 26 jours cumulés en deux épisodes, 2025), pesticides classés A (7 prélèvements, conformité 100%). Ces données de 2025 ne documentent pas un événement de février 2026.

### iframe
`<iframe src="https://PSEUDO.github.io/NOM-DU-DEPOT/" title="Qualité de l'eau du robinet en Vendée" width="100%" height="2400" loading="lazy" style="border:0;width:100%"></iframe>`

## Vérifications restantes avant publication
Tester Safari iOS, Chrome Android, Firefox/Chrome Desktop ; tester l'API Geo et les champs/paramètres exacts de l'API Hub'Eau ; vérifier la pagination et l'interprétation des unités ; traiter l'intégralité des résultats hors navigateur, construire les synthèses annuelles UDI, et faire valider les interprétations par l'ARS. Obtenir de Vendée Eau les coordonnées/identifiants officiels des 13 ouvrages et la chaîne production/UDI avant ajout des marqueurs. Tester les largeurs 320, 375, 390, 430, 768 et 1440 px ainsi que l'iframe et les réseaux à plusieurs UDI.
