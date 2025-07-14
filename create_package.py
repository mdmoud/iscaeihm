#!/usr/bin/env python3
"""
Script pour créer un package distributable de l'Analyseur Ergonomique
"""

import os
import shutil
import zipfile
from datetime import datetime

def create_package():
    """Crée un package distributable"""
    print("📦 Création du package distributable...")
    
    # Nom du package
    package_name = f"AnalyseurErgonomique_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    
    # Fichiers à inclure
    files_to_include = [
        'app.py',
        'run.py',
        'config.py',
        'requirements.txt',
        'README.md',
        'INSTALLATION.md',
        'examples.md',
        'start.bat',
        'start.sh',
        '.gitignore'
    ]
    
    # Dossiers à inclure
    folders_to_include = [
        'templates'
    ]
    
    # Créer le dossier du package
    if os.path.exists(package_name):
        shutil.rmtree(package_name)
    os.makedirs(package_name)
    
    # Copier les fichiers
    for file in files_to_include:
        if os.path.exists(file):
            shutil.copy2(file, package_name)
            print(f"✅ Copié: {file}")
        else:
            print(f"⚠️  Fichier manquant: {file}")
    
    # Copier les dossiers
    for folder in folders_to_include:
        if os.path.exists(folder):
            shutil.copytree(folder, os.path.join(package_name, folder))
            print(f"✅ Copié: {folder}/")
        else:
            print(f"⚠️  Dossier manquant: {folder}")
    
    # Créer un fichier d'instructions rapides
    quick_start = f"""# 🚀 Démarrage Rapide - Analyseur Ergonomique

## Installation et Utilisation

### Prérequis
- Python 3.8 ou supérieur
- Chrome ou Chromium
- Connexion Internet

### Démarrage Automatique

**Sur Windows:**
1. Double-cliquez sur `start.bat`
2. L'application se lancera automatiquement
3. Ouvrez http://localhost:5000 dans votre navigateur

**Sur Linux/Mac:**
1. Ouvrez un terminal dans ce dossier
2. Exécutez: `./start.sh`
3. Ouvrez http://localhost:5000 dans votre navigateur

### Démarrage Manuel
```bash
pip install -r requirements.txt
python run.py
```

### Utilisation
1. Entrez l'URL d'un site web (ex: google.com)
2. Cliquez sur "Analyser"
3. Consultez le rapport ergonomique

### Sites de Test Recommandés
- google.com
- github.com
- wikipedia.org
- example.com

## Support
Consultez README.md pour la documentation complète.
"""
    
    with open(os.path.join(package_name, 'DEMARRAGE_RAPIDE.md'), 'w', encoding='utf-8') as f:
        f.write(quick_start)
    
    # Créer l'archive ZIP
    zip_name = f"{package_name}.zip"
    with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(package_name):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, package_name)
                zipf.write(file_path, arcname)
    
    print(f"\n🎉 Package créé avec succès!")
    print(f"📁 Archive: {zip_name}")
    print(f"📂 Dossier: {package_name}/")
    print(f"\n📋 Pour partager:")
    print(f"1. Envoyez le fichier {zip_name}")
    print(f"2. Le destinataire décompresse et suit les instructions")
    
    return zip_name

if __name__ == '__main__':
    create_package() 