#!/usr/bin/env python3
"""
Script pour déployer l'Analyseur Ergonomique sur un serveur web
"""

import os
import shutil
import subprocess
import sys

def deploy_to_heroku():
    """Déploie l'application sur Heroku"""
    print("🚀 Déploiement sur Heroku...")
    
    # Créer le fichier Procfile pour Heroku
    procfile_content = "web: python run.py"
    with open('Procfile', 'w') as f:
        f.write(procfile_content)
    
    # Créer le fichier runtime.txt
    runtime_content = "python-3.9.18"
    with open('runtime.txt', 'w') as f:
        f.write(runtime_content)
    
    # Créer le fichier app.json
    app_json = {
        "name": "Analyseur Ergonomique",
        "description": "Application d'analyse ergonomique des sites web",
        "repository": "https://github.com/votre-username/analyseur-ergonomique",
        "keywords": ["python", "flask", "ergonomie", "web"],
        "env": {
            "FLASK_ENV": {
                "value": "production"
            }
        },
        "buildpacks": [
            {
                "url": "heroku/python"
            }
        ]
    }
    
    import json
    with open('app.json', 'w') as f:
        json.dump(app_json, f, indent=2)
    
    print("✅ Fichiers de déploiement créés")
    print("\n📋 Instructions pour déployer:")
    print("1. Installez Heroku CLI: https://devcenter.heroku.com/articles/heroku-cli")
    print("2. Connectez-vous: heroku login")
    print("3. Créez l'app: heroku create votre-app-name")
    print("4. Déployez: git push heroku main")
    print("5. Ouvrez: heroku open")

def deploy_to_railway():
    """Déploie l'application sur Railway"""
    print("🚂 Déploiement sur Railway...")
    
    # Créer le fichier railway.json
    railway_config = {
        "build": {
            "builder": "nixpacks"
        },
        "deploy": {
            "startCommand": "python run.py",
            "restartPolicyType": "ON_FAILURE",
            "restartPolicyMaxRetries": 10
        }
    }
    
    import json
    with open('railway.json', 'w') as f:
        json.dump(railway_config, f, indent=2)
    
    print("✅ Fichier railway.json créé")
    print("\n📋 Instructions pour déployer:")
    print("1. Allez sur https://railway.app")
    print("2. Connectez-vous avec GitHub")
    print("3. Créez un nouveau projet")
    print("4. Sélectionnez ce repository")
    print("5. Railway déploiera automatiquement")

def create_deployment_files():
    """Crée tous les fichiers nécessaires pour le déploiement"""
    print("📦 Création des fichiers de déploiement...")
    
    # Créer le fichier .env.example
    env_example = """# Configuration de l'application
FLASK_ENV=production
SECRET_KEY=votre-cle-secrete-ici
PORT=5000

# Configuration Selenium
SELENIUM_TIMEOUT=10
SELENIUM_WINDOW_SIZE=1920,1080

# Configuration de l'analyse
MAX_ANALYSIS_TIME=30
"""
    
    with open('.env.example', 'w', encoding='utf-8') as f:
        f.write(env_example)
    
    # Créer le fichier .dockerignore
    dockerignore = """__pycache__
*.pyc
*.pyo
*.pyd
.Python
env
pip-log.txt
pip-delete-this-directory.txt
.tox
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*.cover
*.log
.git
.mypy_cache
.pytest_cache
.hypothesis
.DS_Store
"""
    
    with open('.dockerignore', 'w') as f:
        f.write(dockerignore)
    
    print("✅ Fichiers de déploiement créés")
    print("\n📋 Options de déploiement disponibles:")
    print("1. Heroku: python deploy_web.py --heroku")
    print("2. Railway: python deploy_web.py --railway")
    print("3. Docker: docker-compose up -d")
    print("4. Serveur local: python run.py")

if __name__ == '__main__':
    if len(sys.argv) > 1:
        if sys.argv[1] == '--heroku':
            deploy_to_heroku()
        elif sys.argv[1] == '--railway':
            deploy_to_railway()
        else:
            print("Usage: python deploy_web.py [--heroku|--railway]")
    else:
        create_deployment_files() 