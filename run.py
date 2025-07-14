#!/usr/bin/env python3
"""
Script de démarrage pour l'Analyseur Ergonomique
"""

import os
import sys
from app import app

def main():
    """Fonction principale de démarrage"""
    print("🚀 Démarrage de l'Analyseur Ergonomique...")
    print("=" * 50)
    
    # Vérifier les dépendances
    try:
        import flask
        import requests
        import selenium
        import bs4
        print("✅ Toutes les dépendances sont installées")
    except ImportError as e:
        print(f"❌ Dépendance manquante: {e}")
        print("💡 Exécutez: pip install -r requirements.txt")
        sys.exit(1)
    
    # Configuration
    port = int(os.environ.get('PORT', 5000))
    host = os.environ.get('HOST', '0.0.0.0')
    debug = os.environ.get('FLASK_DEBUG', 'True').lower() == 'true'
    
    print(f"🌐 Serveur accessible sur: http://localhost:{port}")
    print(f"🔧 Mode debug: {'Activé' if debug else 'Désactivé'}")
    print("=" * 50)
    print("📝 Instructions:")
    print("1. Ouvrez votre navigateur")
    print("2. Allez à http://localhost:5000")
    print("3. Entrez l'URL d'un site web à analyser")
    print("4. Cliquez sur 'Analyser'")
    print("=" * 50)
    print("⏹️  Pour arrêter le serveur: Ctrl+C")
    print("=" * 50)
    
    try:
        app.run(host=host, port=port, debug=debug)
    except KeyboardInterrupt:
        print("\n👋 Arrêt du serveur...")
    except Exception as e:
        print(f"❌ Erreur lors du démarrage: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main() 