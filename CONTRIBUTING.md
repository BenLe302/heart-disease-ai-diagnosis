# 🤝 Guide de Contribution

> Merci de votre intérêt pour contribuer au **Système de Diagnostic Cardiaque par IA** !

Ce guide vous explique comment contribuer efficacement à ce projet développé par **Dady Akrou Cyrille**, diplômé de l'**UQTR**.

---

## 📋 Table des Matières

1. [Code de Conduite](#-code-de-conduite)
2. [Types de Contributions](#-types-de-contributions)
3. [Avant de Commencer](#-avant-de-commencer)
4. [Configuration de l'Environnement](#️-configuration-de-lenvironnement)
5. [Processus de Contribution](#-processus-de-contribution)
6. [Standards de Code](#-standards-de-code)
7. [Tests](#-tests)
8. [Documentation](#-documentation)
9. [Considérations Médicales](#️-considérations-médicales)
10. [Processus de Révision](#-processus-de-révision)

---

## 📜 Code de Conduite

En participant à ce projet, vous acceptez de respecter notre code de conduite :

### 🤝 Nos Engagements
- **Respect** mutuel et bienveillance
- **Inclusion** de toutes les perspectives
- **Collaboration** constructive
- **Focus** sur l'amélioration de la santé
- **Éthique** médicale et scientifique

### 🚫 Comportements Inacceptables
- Harcèlement ou discrimination
- Langage offensant ou inapproprié
- Partage d'informations médicales sensibles
- Violation de la confidentialité
- Promotion de pratiques médicales dangereuses

---

## 🎯 Types de Contributions

Nous accueillons plusieurs types de contributions :

### 🐛 Correction de Bugs
- Identification et correction d'erreurs
- Amélioration de la robustesse
- Optimisation des performances

### ✨ Nouvelles Fonctionnalités
- Amélioration de l'interface utilisateur
- Nouveaux algorithmes de ML
- Fonctionnalités d'analyse avancées
- Intégrations avec d'autres systèmes

### 📚 Documentation
- Amélioration des guides existants
- Traductions
- Tutoriels et exemples
- Documentation technique

### 🧪 Tests
- Tests unitaires et d'intégration
- Tests de performance
- Validation clinique
- Tests d'accessibilité

### 🔍 Révision de Code
- Révision des Pull Requests
- Suggestions d'amélioration
- Validation de la qualité

---

## 🚀 Avant de Commencer

### 1. 📖 Familiarisez-vous avec le Projet
- Lisez le [README.md](README.md)
- Consultez le [Guide de Présentation](PRESENTATION_GUIDE.md)
- Explorez le [Guide Technique](TECHNICAL_GUIDE.md)
- Testez l'application localement

### 2. 🔍 Vérifiez les Issues Existantes
- Consultez les [issues ouvertes](https://github.com/[username]/[repo]/issues)
- Vérifiez si votre idée n'est pas déjà en cours
- Participez aux discussions existantes

### 3. 💬 Discutez de Votre Idée
- Ouvrez une issue pour les nouvelles fonctionnalités
- Décrivez clairement votre proposition
- Attendez les retours avant de commencer

---

## ⚙️ Configuration de l'Environnement

### 📋 Prérequis
```bash
# Python 3.8+
python --version

# Git
git --version

# (Optionnel) Docker
docker --version
```

### 🔧 Installation

#### 1. Fork et Clone
```bash
# Fork le projet sur GitHub
# Puis clonez votre fork
git clone https://github.com/[votre-username]/heart-disease-ai-diagnosis.git
cd heart-disease-ai-diagnosis
```

#### 2. Configuration de l'Environnement
```bash
# Créer un environnement virtuel
python -m venv venv

# Activer l'environnement
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

# Installer les dépendances
pip install -r requirements.txt

# Installer les outils de développement
pip install pytest black flake8 mypy pre-commit
```

#### 3. Configuration Git
```bash
# Configurer le remote upstream
git remote add upstream https://github.com/[original-username]/heart-disease-ai-diagnosis.git

# Installer les hooks pre-commit
pre-commit install
```

#### 4. Vérification de l'Installation
```bash
# Tester l'application
python start.py

# Lancer les tests
pytest

# Vérifier le style de code
black --check .
flake8 .
```

---

## 🔄 Processus de Contribution

### 1. 🌿 Créer une Branche
```bash
# Synchroniser avec upstream
git fetch upstream
git checkout main
git merge upstream/main

# Créer une nouvelle branche
git checkout -b feature/nom-de-votre-fonctionnalite
# ou
git checkout -b fix/description-du-bug
```

### 2. 💻 Développer
- Implémentez vos changements
- Suivez les standards de code
- Ajoutez des tests
- Mettez à jour la documentation

### 3. ✅ Tester
```bash
# Tests unitaires
pytest

# Tests de style
black .
flake8 .
mypy .

# Tests manuels
python start.py
```

### 4. 📝 Commit
```bash
# Ajouter les fichiers
git add .

# Commit avec message descriptif
git commit -m "feat: ajouter fonctionnalité de prédiction en temps réel"

# Ou pour un bug fix
git commit -m "fix: corriger erreur de validation des données"
```

### 5. 🚀 Push et Pull Request
```bash
# Push vers votre fork
git push origin feature/nom-de-votre-fonctionnalite

# Créer une Pull Request sur GitHub
# Utilisez le template fourni
```

---

## 📏 Standards de Code

### 🐍 Style Python
- **PEP 8** compliance
- **Black** pour le formatage automatique
- **Flake8** pour le linting
- **MyPy** pour le type checking

### 📝 Conventions de Nommage
```python
# Variables et fonctions: snake_case
patient_data = load_patient_data()

# Classes: PascalCase
class HeartDiseasePredictor:
    pass

# Constantes: UPPER_CASE
MAX_HEART_RATE = 220

# Fichiers: snake_case.py
# heart_disease_model.py
```

### 📋 Documentation du Code
```python
def predict_heart_disease(patient_data: dict) -> dict:
    """
    Prédit la probabilité de maladie cardiaque pour un patient.
    
    Args:
        patient_data (dict): Données cliniques du patient
        
    Returns:
        dict: Résultats de prédiction avec probabilité et facteurs de risque
        
    Raises:
        ValueError: Si les données patient sont invalides
        
    Example:
        >>> data = {'age': 45, 'sex': 1, 'cp': 2}
        >>> result = predict_heart_disease(data)
        >>> print(result['probability'])
        0.75
    """
    pass
```

### 🔧 Structure des Commits
```
type(scope): description courte

Description plus détaillée si nécessaire.

Fixes #123
```

**Types de commits :**
- `feat`: nouvelle fonctionnalité
- `fix`: correction de bug
- `docs`: documentation
- `style`: formatage
- `refactor`: refactoring
- `test`: tests
- `chore`: maintenance

---

## 🧪 Tests

### 📋 Types de Tests Requis

#### 1. Tests Unitaires
```python
import pytest
from app.prediction import HeartDiseasePredictor

def test_prediction_valid_data():
    """Test prédiction avec données valides."""
    predictor = HeartDiseasePredictor()
    data = {
        'age': 45,
        'sex': 1,
        'cp': 2,
        # ... autres paramètres
    }
    result = predictor.predict(data)
    
    assert 'probability' in result
    assert 0 <= result['probability'] <= 1
    assert 'risk_factors' in result

def test_prediction_invalid_data():
    """Test prédiction avec données invalides."""
    predictor = HeartDiseasePredictor()
    
    with pytest.raises(ValueError):
        predictor.predict({'age': -5})  # Âge invalide
```

#### 2. Tests d'Intégration
```python
def test_streamlit_app_loads():
    """Test que l'application Streamlit se charge correctement."""
    # Test de l'interface utilisateur
    pass

def test_model_pipeline():
    """Test du pipeline complet de prédiction."""
    # Test de bout en bout
    pass
```

#### 3. Tests de Performance
```python
import time

def test_prediction_performance():
    """Test que la prédiction est rapide."""
    predictor = HeartDiseasePredictor()
    data = get_sample_data()
    
    start_time = time.time()
    result = predictor.predict(data)
    end_time = time.time()
    
    assert end_time - start_time < 1.0  # Moins d'1 seconde
```

### 🎯 Couverture de Tests
- **Minimum 80%** de couverture de code
- **100%** pour les fonctions critiques de prédiction
- Tests pour tous les cas d'erreur

### ▶️ Exécution des Tests
```bash
# Tous les tests
pytest

# Tests avec couverture
pytest --cov=app --cov-report=html

# Tests spécifiques
pytest tests/test_prediction.py

# Tests en mode verbose
pytest -v
```

---

## 📚 Documentation

### 📝 Types de Documentation

#### 1. Docstrings
- **Toutes les fonctions publiques** doivent avoir des docstrings
- Format **Google Style** ou **NumPy Style**
- Inclure exemples d'utilisation

#### 2. README et Guides
- Mettre à jour si votre changement affecte l'utilisation
- Ajouter des exemples pour les nouvelles fonctionnalités
- Maintenir la cohérence du style

#### 3. Commentaires de Code
```python
# Bon commentaire : explique le POURQUOI
# Utilisation de MinMaxScaler car les features ont des échelles différentes
scaler = MinMaxScaler()

# Mauvais commentaire : explique le QUOI (évident)
# Création d'un scaler
scaler = MinMaxScaler()
```

### 🌍 Traductions
Nous accueillons les traductions :
- **Français** (langue principale)
- **Anglais** (langue secondaire)
- **Autres langues** bienvenues

---

## 🏥 Considérations Médicales

### ⚠️ Responsabilités Importantes

#### 1. Avertissements Obligatoires
Tout code lié aux prédictions médicales doit inclure :
```python
def predict_heart_disease(data):
    """
    AVERTISSEMENT MÉDICAL:
    Cet outil est destiné à l'aide à la décision uniquement.
    Il ne remplace pas l'expertise médicale professionnelle.
    Toujours consulter un professionnel de santé qualifié.
    """
    pass
```

#### 2. Validation Clinique
- Nouvelles métriques : validation par professionnel de santé
- Changements d'algorithmes : tests rigoureux
- Seuils de décision : justification clinique

#### 3. Confidentialité des Données
- **Jamais** de vraies données patients dans le code
- Données de test : anonymisées et synthétiques
- Respect du RGPD et des normes médicales

### 🔒 Sécurité Médicale
```python
# ✅ Bon : validation des entrées
def validate_patient_data(data):
    if data.get('age', 0) < 0 or data.get('age', 0) > 150:
        raise ValueError("Âge invalide")
    
    if data.get('cholesterol', 0) < 0:
        raise ValueError("Cholestérol invalide")

# ❌ Mauvais : pas de validation
def predict_without_validation(data):
    return model.predict(data)  # Dangereux !
```

---

## 🔍 Processus de Révision

### 👥 Qui Révise ?
- **Dady Akrou Cyrille** (mainteneur principal)
- **Contributeurs expérimentés**
- **Experts médicaux** (pour changements cliniques)

### 📋 Critères de Révision

#### ✅ Critères Techniques
- [ ] Code suit les standards du projet
- [ ] Tests passent et couverture maintenue
- [ ] Documentation mise à jour
- [ ] Pas de régression de performance
- [ ] Sécurité respectée

#### 🏥 Critères Médicaux
- [ ] Avertissements médicaux présents
- [ ] Validation clinique appropriée
- [ ] Pas de risque pour la sécurité patient
- [ ] Conformité aux standards médicaux

#### 📚 Critères de Documentation
- [ ] Docstrings complètes
- [ ] Exemples d'utilisation clairs
- [ ] Guides mis à jour si nécessaire

### ⏱️ Délais de Révision
- **Bugs critiques** : 24-48h
- **Nouvelles fonctionnalités** : 3-7 jours
- **Documentation** : 1-3 jours
- **Changements majeurs** : 1-2 semaines

### 🔄 Processus de Révision
1. **Révision automatique** (CI/CD)
2. **Révision technique** (code, tests)
3. **Révision médicale** (si applicable)
4. **Tests finaux** et validation
5. **Merge** et déploiement

---

## 🎯 Conseils pour les Nouveaux Contributeurs

### 🚀 Commencer Petit
- Corrigez d'abord des bugs simples
- Améliorez la documentation
- Ajoutez des tests
- Participez aux discussions

### 📖 Ressources d'Apprentissage
- [Documentation Streamlit](https://docs.streamlit.io/)
- [Scikit-learn User Guide](https://scikit-learn.org/stable/user_guide.html)
- [Guide PEP 8](https://pep8.org/)
- [Pytest Documentation](https://docs.pytest.org/)

### 🤝 Communauté
- Soyez patient et respectueux
- Posez des questions si vous ne comprenez pas
- Aidez les autres contributeurs
- Partagez vos connaissances

---

## 📞 Support et Contact

### 💬 Où Obtenir de l'Aide ?
- **Issues GitHub** : Questions techniques
- **Discussions** : Idées et suggestions
- **Email** : [votre-email@example.com]

### 🐛 Signaler des Problèmes
1. Vérifiez les issues existantes
2. Utilisez les templates fournis
3. Fournissez des détails complets
4. Incluez des exemples reproductibles

### 💡 Proposer des Idées
1. Ouvrez une issue "Feature Request"
2. Décrivez clairement le besoin
3. Proposez une solution
4. Discutez avec la communauté

---

## 🙏 Remerciements

Merci à tous les contributeurs qui aident à améliorer ce projet !

### 🌟 Contributeurs Principaux
- **Dady Akrou Cyrille** - Créateur et mainteneur principal
- [Votre nom ici] - Première contribution

### 🏆 Types de Reconnaissance
- **Mention** dans le README
- **Badge** de contributeur
- **Certificat** de contribution (sur demande)
- **Recommandation** LinkedIn

---

## 📜 Licence

En contribuant à ce projet, vous acceptez que vos contributions soient sous la même licence que le projet principal.

---

**🫀 Ensemble, améliorons le diagnostic cardiaque par l'IA ! 🚀**

*Guide de contribution maintenu par Dady Akrou Cyrille - UQTR Data Science Graduate*