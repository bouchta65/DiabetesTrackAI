# DiabetesTrackAI

**Statut** : Prototype · Machine Learning · Streamlit

## Description

Vous êtes un développeur IA junior au sein d’un laboratoire biomédical. DiabetesTrackAI est un projet visant à concevoir, entraîner et déployer un système intelligent capable :

* de **classer** les patients selon leur risque de diabète (risque élevé / faible) ;
* de **regrouper (clustering)** les données pour identifier des profils de patients similaires.

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
