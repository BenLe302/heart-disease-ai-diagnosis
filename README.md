# 🫀 Heart Disease Prediction System

[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)](https://streamlit.io/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Production-brightgreen.svg)]()

## 📋 Overview

A comprehensive machine learning system for predicting heart disease using the UCI Heart Disease dataset. This project implements multiple ML algorithms with clinical validation and provides an intuitive web interface for healthcare professionals.

## 🎯 Key Features

- **Multiple ML Models**: Logistic Regression, Random Forest, XGBoost, CatBoost
- **Clinical Validation**: Medically-relevant metrics and interpretability
- **Interactive Dashboard**: Streamlit-based web application
- **REST API**: FastAPI backend for integration
- **Comprehensive Analysis**: Feature importance, SHAP values, clinical insights
- **Production Ready**: Docker support, testing, and monitoring

## 🏗️ Project Structure

```
heart-disease-prediction/
├── data/
│   ├── raw/                    # Original dataset
│   └── processed/              # Preprocessed data
├── notebooks/
│   ├── 01_data_exploration.ipynb
│   ├── 02_preprocessing.ipynb
│   ├── 03_model_training.ipynb
│   └── 04_clinical_analysis.ipynb
├── src/
│   ├── data/
│   │   ├── preprocessing.py
│   │   └── validation.py
│   ├── models/
│   │   ├── training.py
│   │   ├── evaluation.py
│   │   └── prediction.py
│   ├── api/
│   │   ├── main.py
│   │   └── schemas.py
│   └── utils/
│       ├── config.py
│       └── helpers.py
├── app/
│   └── streamlit_app.py        # Main dashboard
├── models/                     # Trained models
├── tests/                      # Unit tests
├── docker/                     # Docker configuration
├── requirements.txt
└── README.md
```

## 🚀 Quick Start

### Prerequisites

- Python 3.11+
- pip or conda
- Git

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/heart-disease-prediction.git
   cd heart-disease-prediction
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   streamlit run app/streamlit_app.py
   ```

### Using Docker

```bash
docker build -t heart-disease-app .
docker run -p 8501:8501 heart-disease-app
```

## 📊 Dataset Information

**Source**: UCI Heart Disease Dataset  
**Samples**: 1,025 patients  
**Features**: 13 clinical parameters  
**Target**: Binary classification (heart disease presence)

### Key Features:
- **age**: Age in years
- **sex**: Gender (M/F)
- **cp**: Chest pain type
- **trestbps**: Resting blood pressure
- **chol**: Serum cholesterol
- **fbs**: Fasting blood sugar
- **restecg**: Resting ECG results
- **thalach**: Maximum heart rate achieved
- **exang**: Exercise induced angina
- **oldpeak**: ST depression induced by exercise
- **slope**: Slope of peak exercise ST segment
- **ca**: Number of major vessels colored by fluoroscopy
- **thal**: Thalassemia type

## 🤖 Model Performance

| Model | Accuracy | Precision | Recall | F1-Score | AUC-ROC |
|-------|----------|-----------|--------|----------|----------|
| CatBoost | 87.3% | 89.1% | 85.2% | 87.1% | 0.923 |
| XGBoost | 86.8% | 88.4% | 84.7% | 86.5% | 0.918 |
| Random Forest | 85.9% | 87.2% | 83.8% | 85.5% | 0.912 |
| Logistic Regression | 83.4% | 85.1% | 81.3% | 83.2% | 0.895 |

## 🔬 Clinical Insights

### Most Important Risk Factors:
1. **Chest Pain Type (cp)** - 23.4% importance
2. **Maximum Heart Rate (thalach)** - 18.7% importance
3. **ST Depression (oldpeak)** - 15.2% importance
4. **Number of Major Vessels (ca)** - 12.8% importance
5. **Thalassemia (thal)** - 11.3% importance

### Clinical Thresholds:
- **High Risk**: Probability > 0.7
- **Moderate Risk**: 0.3 < Probability ≤ 0.7
- **Low Risk**: Probability ≤ 0.3

## 🖥️ Web Application

The Streamlit dashboard provides:

- **Patient Input Form**: Easy data entry for clinical parameters
- **Real-time Prediction**: Instant risk assessment
- **Probability Visualization**: Gauge charts and confidence intervals
- **Feature Importance**: SHAP explanations for individual predictions
- **Clinical Recommendations**: Actionable insights based on risk factors
- **Data Visualization**: Interactive charts and statistical analysis

## 🔌 API Usage

### Start the API server:
```bash
uvicorn src.api.main:app --reload
```

### Make predictions:
```python
import requests

data = {
    "age": 63,
    "sex": "Male",
    "cp": "Typical Angina",
    "trestbps": 145,
    "chol": 233,
    "fbs": "False",
    "restecg": "Normal",
    "thalach": 150,
    "exang": "False",
    "oldpeak": 2.3,
    "slope": "Downsloping",
    "ca": 0,
    "thal": "Normal"
}

response = requests.post("http://localhost:8000/predict", json=data)
print(response.json())
```

## 🧪 Testing

Run the test suite:
```bash
pytest tests/ -v
```

Run with coverage:
```bash
pytest tests/ --cov=src --cov-report=html
```

## 📈 Model Training

To retrain models with new data:

```bash
python src/models/training.py --config config/training_config.yaml
```

## 🐳 Deployment

### Docker Compose
```bash
docker-compose up -d
```

### Cloud Deployment
The application is ready for deployment on:
- **Streamlit Cloud**
- **Heroku**
- **AWS ECS**
- **Google Cloud Run**
- **Azure Container Instances**

## 📝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- UCI Machine Learning Repository for the dataset
- The medical community for clinical validation insights
- Open source contributors and maintainers

## 📞 Contact

**Project Maintainer**: Data Science Team  
**Email**: contact@heartdisease-prediction.com  
**Issues**: [GitHub Issues](https://github.com/your-username/heart-disease-prediction/issues)

---

⚠️ **Medical Disclaimer**: This tool is for educational and research purposes only. It should not be used as a substitute for professional medical advice, diagnosis, or treatment. Always consult with qualified healthcare providers for medical decisions.