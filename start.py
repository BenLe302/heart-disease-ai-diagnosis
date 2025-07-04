#!/usr/bin/env python3
"""
Script de démarrage rapide pour le projet de diagnostic cardiaque

Usage:
    python start.py --help
    python start.py --install
    python start.py --app
    python start.py --notebook
    python start.py --train
"""

import argparse
import subprocess
import sys
import os
from pathlib import Path

def run_command(command, description):
    """Exécute une commande et affiche le résultat"""
    print(f"\n🚀 {description}...")
    print(f"Commande: {' '.join(command)}")
    
    try:
        result = subprocess.run(command, check=True, capture_output=True, text=True)
        print(f"✅ {description} terminé avec succès")
        if result.stdout:
            print(f"Output: {result.stdout}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Erreur lors de {description}")
        print(f"Code d'erreur: {e.returncode}")
        if e.stderr:
            print(f"Erreur: {e.stderr}")
        return False
    except FileNotFoundError:
        print(f"❌ Commande non trouvée. Assurez-vous que les outils nécessaires sont installés.")
        return False

def install_dependencies():
    """Installe les dépendances du projet"""
    print("📦 Installation des dépendances...")
    
    # Vérifier si requirements.txt existe
    if not Path("requirements.txt").exists():
        print("❌ Fichier requirements.txt non trouvé")
        return False
    
    # Installer les dépendances
    return run_command([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"], 
                      "Installation des dépendances")

def start_streamlit_app():
    """Lance l'application Streamlit"""
    app_path = Path("app/streamlit_app.py")
    
    if not app_path.exists():
        print("❌ Fichier streamlit_app.py non trouvé dans le dossier app/")
        return False
    
    print("\n🌐 Lancement de l'application Streamlit...")
    print("L'application sera disponible à l'adresse: http://localhost:8501")
    print("Appuyez sur Ctrl+C pour arrêter l'application")
    
    try:
        subprocess.run(["streamlit", "run", str(app_path)], check=True)
    except KeyboardInterrupt:
        print("\n👋 Application arrêtée par l'utilisateur")
    except FileNotFoundError:
        print("❌ Streamlit non trouvé. Installez-le avec: pip install streamlit")
        return False
    
    return True

def start_jupyter():
    """Lance Jupyter Lab"""
    notebooks_path = Path("notebooks")
    
    if not notebooks_path.exists():
        print("❌ Dossier notebooks/ non trouvé")
        return False
    
    print("\n📓 Lancement de Jupyter Lab...")
    print("Jupyter Lab s'ouvrira dans votre navigateur")
    print("Appuyez sur Ctrl+C pour arrêter Jupyter")
    
    try:
        subprocess.run(["jupyter", "lab", "notebooks/"], check=True)
    except KeyboardInterrupt:
        print("\n👋 Jupyter arrêté par l'utilisateur")
    except FileNotFoundError:
        print("❌ Jupyter non trouvé. Installez-le avec: pip install jupyterlab")
        return False
    
    return True

def train_models():
    """Lance l'entraînement des modèles"""
    notebook_path = Path("notebooks/01_heart_disease_complete_analysis.ipynb")
    
    if not notebook_path.exists():
        print("❌ Notebook d'analyse non trouvé")
        return False
    
    print("\n🤖 Lancement de l'entraînement des modèles...")
    print("Cela peut prendre plusieurs minutes...")
    
    # Convertir et exécuter le notebook
    return run_command(["jupyter", "nbconvert", "--to", "notebook", "--execute", 
                       str(notebook_path), "--output", "executed_analysis.ipynb"], 
                      "Entraînement des modèles")

def check_environment():
    """Vérifie l'environnement de développement"""
    print("🔍 Vérification de l'environnement...")
    
    # Vérifier Python
    python_version = sys.version_info
    print(f"Python: {python_version.major}.{python_version.minor}.{python_version.micro}")
    
    if python_version < (3, 8):
        print("⚠️  Python 3.8+ recommandé")
    
    # Vérifier les fichiers essentiels
    essential_files = [
        "requirements.txt",
        "README.md",
        "app/streamlit_app.py",
        "notebooks/01_heart_disease_complete_analysis.ipynb"
    ]
    
    missing_files = []
    for file_path in essential_files:
        if not Path(file_path).exists():
            missing_files.append(file_path)
        else:
            print(f"✅ {file_path}")
    
    if missing_files:
        print(f"\n❌ Fichiers manquants: {', '.join(missing_files)}")
        return False
    
    print("\n✅ Environnement prêt!")
    return True

def main():
    parser = argparse.ArgumentParser(
        description="Script de démarrage pour le projet de diagnostic cardiaque",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Exemples d'utilisation:
  python start.py --install          # Installer les dépendances
  python start.py --app              # Lancer l'application Streamlit
  python start.py --notebook         # Lancer Jupyter Lab
  python start.py --train            # Entraîner les modèles
  python start.py --check            # Vérifier l'environnement
        """
    )
    
    parser.add_argument("--install", action="store_true", 
                       help="Installer les dépendances")
    parser.add_argument("--app", action="store_true", 
                       help="Lancer l'application Streamlit")
    parser.add_argument("--notebook", action="store_true", 
                       help="Lancer Jupyter Lab")
    parser.add_argument("--train", action="store_true", 
                       help="Entraîner les modèles")
    parser.add_argument("--check", action="store_true", 
                       help="Vérifier l'environnement")
    
    args = parser.parse_args()
    
    # Si aucun argument, afficher l'aide
    if not any(vars(args).values()):
        parser.print_help()
        return
    
    print("🏥 Projet de Diagnostic Cardiaque")
    print("=" * 40)
    
    success = True
    
    if args.check:
        success &= check_environment()
    
    if args.install:
        success &= install_dependencies()
    
    if args.train:
        success &= train_models()
    
    if args.notebook:
        success &= start_jupyter()
    
    if args.app:
        success &= start_streamlit_app()
    
    if success:
        print("\n🎉 Opération terminée avec succès!")
    else:
        print("\n❌ Des erreurs se sont produites")
        sys.exit(1)

if __name__ == "__main__":
    main()