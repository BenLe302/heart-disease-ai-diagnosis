# Makefile pour le projet de diagnostic cardiaque

.PHONY: help install run test clean docker-build docker-run notebook format lint

# Variables
PYTHON = python
PIP = pip
STREAMLIT = streamlit
DOCKER = docker
IMAGE_NAME = heart-disease-diagnosis
CONTAINER_NAME = heart-disease-app

# Aide
help:
	@echo "Commandes disponibles:"
	@echo "  install     - Installer les dépendances"
	@echo "  run         - Lancer l'application Streamlit"
	@echo "  notebook    - Lancer Jupyter Lab"
	@echo "  test        - Exécuter les tests"
	@echo "  format      - Formater le code avec black"
	@echo "  lint        - Vérifier le code avec flake8"
	@echo "  clean       - Nettoyer les fichiers temporaires"
	@echo "  docker-build - Construire l'image Docker"
	@echo "  docker-run  - Lancer le conteneur Docker"

# Installation des dépendances
install:
	$(PIP) install -r requirements.txt
	@echo "✅ Dépendances installées"

# Lancement de l'application Streamlit
run:
	$(STREAMLIT) run app/streamlit_app.py

# Lancement de Jupyter Lab
notebook:
	jupyter lab notebooks/

# Tests
test:
	$(PYTHON) -m pytest tests/ -v
	@echo "✅ Tests exécutés"

# Formatage du code
format:
	black app/ src/ tests/
	@echo "✅ Code formaté"

# Vérification du code
lint:
	flake8 app/ src/ tests/
	@echo "✅ Code vérifié"

# Nettoyage
clean:
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
	find . -type d -name ".pytest_cache" -delete
	find . -type f -name ".coverage" -delete
	@echo "✅ Fichiers temporaires supprimés"

# Construction de l'image Docker
docker-build:
	$(DOCKER) build -t $(IMAGE_NAME) .
	@echo "✅ Image Docker construite"

# Lancement du conteneur Docker
docker-run:
	$(DOCKER) run -p 8501:8501 --name $(CONTAINER_NAME) $(IMAGE_NAME)

# Arrêt et suppression du conteneur
docker-stop:
	$(DOCKER) stop $(CONTAINER_NAME) || true
	$(DOCKER) rm $(CONTAINER_NAME) || true
	@echo "✅ Conteneur arrêté et supprimé"

# Installation en mode développement
dev-install: install
	$(PIP) install -e .
	@echo "✅ Installation en mode développement"

# Mise à jour des dépendances
update:
	$(PIP) install --upgrade -r requirements.txt
	@echo "✅ Dépendances mises à jour"