# Correction de l’automatisation ARS

La copie envoyée possède `workflows/actualisation-ars.yml` à un emplacement que GitHub Actions ne reconnaît pas. Le fichier doit être dans `.github/workflows/actualisation-ars.yml`. Ce ZIP le place au bon endroit.

## Installer avec le moins de manipulations

1. Ouvrir le dépôt sur GitHub.
2. Dans **Code**, cliquer **Add file > Create new file**.
3. Dans le nom du nouveau fichier, coller `.github/workflows/actualisation-ars.yml`.
4. Copier le contenu de ce fichier depuis le ZIP, puis **Commit changes**.
5. Ouvrir **Actions > Actualiser notes ARS 2025 > Run workflow**.
6. Si l’exécution échoue, ouvrir le journal et conserver la capture de l’erreur.
7. Si elle réussit, vérifier que `qualite-2025.json` a été mis à jour, en particulier les statistiques `fiches_lues`, `communes_classees` et `communes_multi_notes`.

**Attention :** ce correctif ne télécharge pas à lui seul les bilans ; il rend l’automatisation détectable par GitHub. Le collecteur devra encore pouvoir accéder aux services externes et trouver suffisamment de fiches. Les données de la carte restent partielles jusqu'à validation.
