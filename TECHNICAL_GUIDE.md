# Guide Technique - Diagnostic Cardiaque

## Architecture du Projet

### Structure des Dossiers
```
00 projet medical/
├── .streamlit/          # Configuration Streamlit
├── app/                 # Application web
├── data/                # Données d'exemple
├── notebooks/           # Analyses Jupyter
├── requirements.txt     # Dépendances Python
├── Dockerfile          # Configuration Docker
├── Makefile            # Automatisation des tâches
├── start.py            # Script de démarrage
└── README.md           # Documentation principale
```

## Technologies Utilisées

### Machine Learning
- **Scikit-learn**: Modèles de classification (Random Forest, Logistic Regression, etc.)
- **XGBoost**: Gradient boosting optimisé
- **CatBoost**: Gradient boosting pour données catégorielles
- **Pandas**: Manipulation des données
- **NumPy**: Calculs numériques

### Visualisation
- **Matplotlib**: Graphiques de base
- **Seaborn**: Visualisations statistiques
- **Plotly**: Graphiques interactifs

### Interface Web
- **Streamlit**: Application web interactive
- **HTML/CSS**: Personnalisation de l'interface

### Développement
- **Jupyter**: Notebooks d'analyse
- **Docker**: Conteneurisation
- **Make**: Automatisation des tâches

## Modèles Implémentés

### 1. Logistic Regression
- **Avantages**: Interprétable, rapide
- **Usage**: Baseline et comparaison
- **Hyperparamètres**: C, solver, max_iter

### 2. Random Forest
- **Avantages**: Robuste, feature importance
- **Usage**: Modèle principal
- **Hyperparamètres**: n_estimators, max_depth, min_samples_split

### 3. Gradient Boosting
- **Avantages**: Haute performance
- **Usage**: Comparaison avec Random Forest
- **Hyperparamètres**: n_estimators, learning_rate, max_depth

### 4. XGBoost
- **Avantages**: Optimisé, gestion des valeurs manquantes
- **Usage**: Modèle de production
- **Hyperparamètres**: n_estimators, learning_rate, max_depth, subsample

### 5. CatBoost
- **Avantages**: Gestion native des catégories
- **Usage**: Alternative robuste
- **Hyperparamètres**: iterations, learning_rate, depth

## Pipeline de Données

### 1. Chargement
```python
data = pd.read_csv('data/heart.csv')
```

### 2. Préprocessing
- **Encodage**: Variables catégorielles (sex, cp, restecg, etc.)
- **Normalisation**: StandardScaler pour les variables numériques
- **Division**: Train/Test split (80/20)

### 3. Entraînement
- **Validation croisée**: 5-fold CV
- **Optimisation**: RandomizedSearchCV
- **Métriques**: Accuracy, Precision, Recall, F1, AUC-ROC

### 4. Évaluation
- **Matrice de confusion**
- **Courbes ROC**
- **Feature importance**
- **Classification report**

## API et Endpoints

### Application Streamlit
- **URL**: `http://localhost:8501`
- **Fonctionnalités**:
  - Prédiction individuelle
  - Visualisation des données
  - Interprétation des résultats
  - Métriques de performance

### Fonctions Principales

#### `prepare_input_data()`
```python
def prepare_input_data(age, sex, cp, trestbps, chol, fbs, 
                      restecg, thalach, exang, oldpeak, 
                      slope, ca, thal):
    """Prépare les données d'entrée pour la prédiction"""
```

#### `interpret_risk()`
```python
def interpret_risk(probability):
    """Interprète le niveau de risque"""
```

#### `load_model()`
```python
def load_model(model_path):
    """Charge un modèle sauvegardé"""
```

## Métriques de Performance

### Métriques Cliniques
- **Sensibilité (Recall)**: Capacité à détecter les vrais positifs
- **Spécificité**: Capacité à détecter les vrais négatifs
- **VPP**: Valeur prédictive positive
- **VPN**: Valeur prédictive négative

### Métriques Techniques
- **Accuracy**: Précision globale
- **AUC-ROC**: Aire sous la courbe ROC
- **F1-Score**: Moyenne harmonique précision/recall
- **Log-Loss**: Perte logarithmique

## Déploiement

### Local
```bash
# Installation
python start.py --install

# Lancement
python start.py --app
```

### Docker
```bash
# Construction
docker build -t heart-disease-app .

# Lancement
docker run -p 8501:8501 heart-disease-app
```

### Production
- **Streamlit Cloud**: Déploiement direct depuis GitHub
- **Heroku**: Avec Dockerfile
- **AWS/GCP**: Instances cloud

## Tests et Validation

### Tests Unitaires
```python
# Test de préparation des données
def test_prepare_input_data():
    # Test avec données valides
    # Test avec données manquantes
    # Test avec valeurs aberrantes
```

### Validation Croisée
- **K-Fold**: 5 plis
- **Stratified**: Préservation des proportions
- **Time Series**: Si données temporelles

### Tests d'Intégration
- **API**: Tests des endpoints
- **UI**: Tests de l'interface
- **Performance**: Tests de charge

## Monitoring et Maintenance

### Métriques à Surveiller
- **Performance du modèle**: AUC, Accuracy
- **Dérive des données**: Distribution des features
- **Latence**: Temps de réponse
- **Erreurs**: Taux d'erreur

### Mise à Jour du Modèle
1. **Collecte de nouvelles données**
2. **Validation de la qualité**
3. **Réentraînement**
4. **Tests A/B**
5. **Déploiement progressif**

## Sécurité

### Données Sensibles
- **Anonymisation**: Suppression des identifiants
- **Chiffrement**: Données en transit et au repos
- **Accès**: Contrôle des permissions

### Application
- **HTTPS**: Connexions sécurisées
- **Validation**: Inputs utilisateur
- **Logs**: Audit des accès

## Optimisations

### Performance
- **Caching**: Mise en cache des prédictions
- **Batch Processing**: Traitement par lots
- **Model Compression**: Réduction de la taille

### Scalabilité
- **Load Balancing**: Répartition de charge
- **Microservices**: Architecture modulaire
- **Auto-scaling**: Adaptation automatique

## Troubleshooting

### Erreurs Communes

#### Erreur de Dépendances
```bash
# Solution
pip install --upgrade -r requirements.txt
```

#### Erreur de Modèle
```python
# Vérifier l'existence du fichier
if not os.path.exists(model_path):
    print("Modèle non trouvé")
```

#### Erreur de Données
```python
# Validation des inputs
if age < 0 or age > 120:
    raise ValueError("Âge invalide")
```

### Logs
- **Application**: `logs/app.log`
- **Modèle**: `logs/model.log`
- **Erreurs**: `logs/error.log`

## Contact et Support

- **Documentation**: README.md
- **Issues**: GitHub Issues
- **Email**: [votre-email]
- **Wiki**: Documentation détaillée

---

**Note**: Ce guide technique est destiné aux développeurs et data scientists travaillant sur le projet.