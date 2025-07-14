# Guide d'Installation Rapide - Analyseur Ergonomique

## 🚀 Démarrage Rapide

### Sur Windows
1. Double-cliquez sur `start.bat`
2. L'application se lancera automatiquement
3. Ouvrez votre navigateur sur `http://localhost:5000`

### Sur Linux/Mac
1. Ouvrez un terminal dans le dossier du projet
2. Exécutez : `./start.sh`
3. Ouvrez votre navigateur sur `http://localhost:5000`

### Manuellement
```bash
# Installer les dépendances
pip install Flask requests beautifulsoup4 selenium webdriver-manager

# Démarrer l'application
python run.py
```

## 📋 Prérequis

- **Python 3.8+** : [Télécharger Python](https://python.org)
- **Chrome/Chromium** : Pour l'analyse des sites web
- **Connexion Internet** : Pour analyser les sites web

## 🔧 Configuration

### Variables d'environnement (optionnel)
```bash
# Port du serveur (défaut: 5000)
export PORT=8080

# Mode debug (défaut: True)
export FLASK_DEBUG=False

# Clé secrète (défaut: auto-générée)
export SECRET_KEY=votre-cle-secrete
```

## 🧪 Test de l'Application

Après le démarrage, testez avec :
```bash
python test_app.py
```

## 📁 Structure du Projet

```
ErgoAutoEvaluation/
├── app.py              # Application principale
├── run.py              # Script de démarrage
├── config.py           # Configuration
├── requirements.txt    # Dépendances Python
├── templates/
│   └── index.html     # Interface utilisateur
├── start.bat          # Démarrage Windows
├── start.sh           # Démarrage Linux/Mac
├── test_app.py        # Tests
├── examples.md        # Exemples d'utilisation
├── README.md          # Documentation complète
└── INSTALLATION.md    # Ce fichier
```

## 🐛 Dépannage

### Erreur "Python non trouvé"
- Installez Python depuis [python.org](https://python.org)
- Ajoutez Python au PATH système

### Erreur "Module non trouvé"
```bash
pip install -r requirements.txt
```

### Erreur "Port déjà utilisé"
- Changez le port : `export PORT=8080`
- Ou arrêtez l'application qui utilise le port 5000

### Erreur Selenium
- Installez Chrome/Chromium
- Le driver sera téléchargé automatiquement

## 📞 Support

- Consultez `README.md` pour la documentation complète
- Consultez `examples.md` pour des exemples d'utilisation
- Vérifiez les logs dans la console pour les erreurs

## 🎯 Utilisation

1. **Ouvrez** `http://localhost:5000`
2. **Entrez** l'URL d'un site web
3. **Cliquez** sur "Analyser"
4. **Consultez** le rapport ergonomique
5. **Exportez** les résultats si nécessaire

## 🔄 Mise à Jour

```bash
# Mettre à jour les dépendances
pip install --upgrade -r requirements.txt

# Redémarrer l'application
python run.py
``` 