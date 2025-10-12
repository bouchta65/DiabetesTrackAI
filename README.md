# DiabetesTrackAI

**Statut** : Prototype · Machine Learning · Streamlit

## Description

DiabetesTrack_AI est un projet d’intelligence artificielle dédié à l’analyse et à la prédiction du risque de diabète chez les patients. Il utilise des techniques de clustering pour segmenter les profils de patients et des modèles de classification supervisée (Random Forest, SVM, XGBoost, etc.) pour prédire avec précision le risque de diabète.

Le modèle s'appuie sur des critères cliniques usuels : **Glucose, BloodPressure, SkinThickness, Insulin, BMI, Diabetes Pedigree Function, Age**, et d'autres colonnes présentes dans le jeu de données historique du laboratoire.

## Objectifs (User Stories)

1. **Chargement & EDA** — importer les données, analyser la structure, valeurs manquantes, distributions et corrélations.
2. **Prétraitement** — gérer valeurs manquantes, détecter et traiter outliers, normaliser/standardiser.
3. **Clustering (K-Means)** — déterminer k optimal (méthode du coude, silhouette), entraîner K-Means, ajouter colonne `Cluster`.
4. **Analyse des clusters** — interpréter les clusters, calculer moyennes, créer `risk_category` (1 = haut risque si seuils dépassés).
5. **Classification supervisée** — utiliser `Cluster` comme cible, tester plusieurs algorithmes (RandomForest, SVM, GradientBoosting, DecisionTree, LogisticRegression, XGBoost), gérer déséquilibre (SMOTE / RandomOverSampler / UnderSampler), validation croisée, recherche d'hyperparamètres, métriques (confusion matrix, accuracy, recall, precision, F1), sauvegarde du meilleur modèle (`model.pkl`).
6. **Documentation & reproductibilité** — commentaires, notebook Markdown, README (ce fichier), planification Jira.
7. **Application Streamlit** — interface utilisateur pour saisir des valeurs et obtenir une prédiction en temps réel + visualisations (position du patient dans les clusters, probabilités, conseils basiques).

---
