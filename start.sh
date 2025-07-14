#!/bin/bash

echo "========================================"
echo "  Analyseur Ergonomique - Démarrage"
echo "========================================"
echo

# Vérifier si Python est installé
if ! command -v python3 &> /dev/null; then
    echo "ERREUR: Python 3 n'est pas installé"
    echo "Veuillez installer Python 3 depuis https://python.org"
    exit 1
fi

echo "Python détecté:"
python3 --version
echo

# Vérifier si les dépendances sont installées
echo "Vérification des dépendances..."
if ! python3 -c "import flask, requests, selenium, bs4" &> /dev/null; then
    echo "Installation des dépendances..."
    pip3 install Flask requests beautifulsoup4 selenium webdriver-manager
    if [ $? -ne 0 ]; then
        echo "ERREUR: Impossible d'installer les dépendances"
        exit 1
    fi
fi

echo
echo "========================================"
echo "  Démarrage du serveur..."
echo "========================================"
echo
echo "L'application sera accessible sur:"
echo "http://localhost:5000"
echo
echo "Pour arrêter le serveur, appuyez sur Ctrl+C"
echo
echo "========================================"
echo

# Démarrer l'application
python3 run.py 