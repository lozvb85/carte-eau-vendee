# Carte de l'eau en Vendée · V10

Projet statique GitHub Pages. **Référence sanitaire : bilans annuels ARS 2025.** Les analyses ponctuelles 2026 sont interrogées séparément auprès de Hub'Eau au clic sur une commune. Ne pas présenter 2025 comme un classement 2026.

## Contenu

- `index.html` : carte Leaflet, navigation, barrages, fiches communes, légende A/B/C/D, recherche et comparaison des barrages.
- `communes-vendee.json` : liste locale de 253 communes et codes INSEE, pour le répertoire même si l'API des contours est temporairement indisponible.
- `qualite-2025.json` : notes **vérifiées** ; dans l'archive initiale, seules les communes Essarts-en-Bocage (C, réseau Frétière Beaulieu) et La Roche-sur-Yon (A, réseau 085000201) sont associées avec certitude. Les fiches A des UDI 085000030 et 085000450 sont recensées, **sans déduire quelles communes elles desservent**.
- `scripts/collecte_ars.py` : outil de collecte à partir des relations commune–UDI Hub'Eau et des PDF Infofacture ARS. Un PDF absent ou ambigu n'est pas classé.
- `.github/workflows/actualisation-ars.yml` : exécution manuelle ou hebdomadaire de l'outil sur GitHub Actions. **Le fonctionnement réel de cette collecte sur le serveur de GitHub n'a pas été vérifié** et dépend de la disponibilité des sources officielles.

## Publier sur GitHub Pages

1. Télécharger puis **extraire** le ZIP.
2. Ouvrir le dépôt `lozvb85/carte-eau-vendee`, branch `main`.
3. Importer les fichiers à la racine du dépôt : `index.html`, `qualite-2025.json`, `communes-vendee.json` ; importer aussi `scripts/collecte_ars.py` et `.github/workflows/actualisation-ars.yml` avec ces chemins exacts. Ne pas importer le dossier parent.
4. Commit changes. Paramètres GitHub Pages : `Deploy from a branch`, `main`, `/(root)`.
5. Tester : https://lozvb85.github.io/carte-eau-vendee/?version=10

**Pour collecter toutes les fiches automatiquement :** dans GitHub, ouvrir **Actions → Actualiser notes ARS 2025 → Run workflow**. Si le bouton n'apparaît pas, autoriser les workflows dans Settings → Actions. Il peut aussi être nécessaire de régler **Settings → Actions → General → Workflow permissions** sur **Read and write permissions**. Un échec de l'action doit être examiné dans ses logs ; le précédent fichier de notes reste en place tant que la collecte échoue.

Le fichier `qualite-2025.json` est ensuite mis à jour par l'action, si toutes les vérifications de couverture passent. Une commune ne reçoit une couleur unique que si **tous ses réseaux connus disposent d'une note et que leurs notes sont identiques**. Si plusieurs réseaux ont des notes différentes, la commune reste grise et les notes sont listées au clic. Les réseaux sans bilan vérifié restent non renseignés.

## Méthode de collecte

1. Lister les 253 codes INSEE à partir du référentiel transmis.
2. Interroger `https://hubeau.eaufrance.fr/api/v1/qualite_eau_potable/communes_udi` avec `code_commune`, `annee=2025`, `size=200`.
3. Dédupliquer les codes de réseaux (UDI).
4. Télécharger les fiches officielles `https://carto.atlasante.fr/IHM/cartes/infofactures/AQUASISED/2025/INFOFACTURE-[CODE_UDI]-2025.pdf`.
5. Extraire **uniquement la lettre dans le cartouche « Indicateur global de qualité »** et confirmer l'année.
6. Écarter tout fichier inaccessible, dont la note est illisible ou ambiguë. La source est enregistrée par UDI.
7. Rattacher les UDI aux communes, sans extrapolation basée sur les noms ou la proximité d'un barrage.

Ce mécanisme est **une base d'automatisation à tester**, et non la preuve que tous les bilans ont déjà été téléchargés. Les PDF peuvent changer de mise en page et exiger une revue de la routine d'extraction avant publication d'un dossier journalistique.

## Déjà vérifié

- Les deux fiches PDF transmises `085000030` (Choletière) et `085000450` (Saint-Vincent-sur-Graon) donnent A, ce que la routine d'extraction reproduit sur ces fichiers locaux.
- Le document ARS Frétière-Beaulieu concerne **2025**, classement C en raison de dépassements de bromates ; la cause exacte de l'incident de février **2026** reste non établie.
- Les 13 retenues et leurs remplissages au **25 octobre 2026** sont des données datées, sans mise à jour automatique dans cette version. Leur position demeure indicative.
- La syntaxe JavaScript passe `node --check`. Le test navigateur automatisé a été bloqué par les restrictions de cet environnement ; **aucun test mobile réel** n'a été exécuté.

## Sources

- DGS / ARS : Infofactures officielles (AtlaSanté), bilans 2025.
- API Hub'Eau Qualité de l'eau potable : liaisons communes-UDI et analyses ponctuelles.
- API Géo de l'État : contours communaux.
- Vendée Eau : niveaux et volumes des 13 retenues au 25 octobre 2026.

## Intégration dans un article Alouette

```html
<iframe src="https://lozvb85.github.io/carte-eau-vendee/" title="Qualité de l'eau et barrages en Vendée — Alouette" loading="lazy" style="width:100%;border:0;max-width:100%;height:1450px" referrerpolicy="strict-origin-when-cross-origin"></iframe>
```

Hauteur à ajuster après test sur smartphone (souvent supérieure à celle du bureau). Aucune donnée personnelle collectée volontairement ; les appels aux API externes peuvent générer leurs propres journaux d'accès.
