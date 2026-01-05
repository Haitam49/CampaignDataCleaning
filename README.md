# Nettoyage des données de campagne marketing avec Pandas

## 📌 Présentation du projet
Ce mini-projet consiste à **nettoyer et prétraiter** un dataset de campagnes marketing à partir d’un fichier CSV.  
L’objectif est de transformer des données brutes et désordonnées en un fichier prêt pour l’analyse grâce à **Python** et **Pandas**.  

C’est un excellent projet à mettre sur un CV pour montrer vos compétences en **data wrangling**.

---

## 🛠️ Outils et bibliothèques
- Python 3.9+
- [Pandas](https://pandas.pydata.org/)
- [NumPy](https://numpy.org/)

🧹 Étapes de nettoyage réalisées

 Nettoyage des noms de colonnes :

-  Suppression des espaces, conversion en minuscules, remplacement des espaces par des underscores.

 Conversion des types & nettoyage monétaire :

-  Suppression des symboles $ et caractères non numériques dans la colonne spend.

-  Conversion en type numérique.

 Standardisation des colonnes catégorielles :

-  Correction des fautes de frappe dans channel (ex: "Facebok" → "Facebook").

-  Remplacement des valeurs invalides (N/A) par NaN.

 Gestion des valeurs booléennes :

-  Uniformisation des valeurs dans active (Yes, 1, Y → True, No, 0 → False).

 Parsing des dates :

-  Conversion des colonnes start_date et end_date en format datetime.

-  Gestion des erreurs et formats incohérents.

 Vérifications d’intégrité logique :

-  Détection des lignes où clicks > impressions.

-  Gestion des cas où end_date < start_date (“time travel”).

 Gestion des valeurs aberrantes (outliers) :

-  Détection des outliers dans la colonne spend via la méthode IQR.

-  Limitation des valeurs extrêmes à un seuil maximal.

Extraction de nouvelles fonctionnalités

-  Extraction de la saison (season) à partir de la colonne campaign_name via regex.

Suppression des colonnes dupliquées

 Sauvegarde du dataset nettoyé :

-  Fichier nettoyé : marketing_campaign_data_cleaned.csv.

✅ Résultat

-  Dataset nettoyé et prêt pour l’analyse ou la visualisation.

-  Colonnes renommées, types corrigés, valeurs aberrantes traitées, valeurs invalides remplacées.

📝 Remarques

-  Aucune variable d’environnement ni clé API nécessaire.

-  Le projet utilise des chemins relatifs pour la portabilité.

💡 Améliorations possibles

-  Ajouter des visualisations d’exploration de données (EDA).

-  Gérer les valeurs manquantes de manière plus intelligente (imputation).

-  Automatiser le nettoyage pour plusieurs fichiers CSV.

-  Intégrer dans un petit tableau de bord ou un pipeline ML.

👤 Auteur

Haitam Boulhna Étudiant en ingénierie informatique 📧 Email : haitamboulhna19@gmail.com

🔗 LinkedIn : www.linkedin.com/in/haitamboulhna POTFOLIO : https://haitamportfolio.vercel.app/
