#!/usr/bin/env python3
"""
Test simple pour vérifier le fonctionnement de l'application
"""

import requests
import time

def test_application():
    """Test de base de l'application"""
    print("🧪 Test de l'application d'analyse ergonomique...")
    
    # Attendre que le serveur démarre
    print("⏳ Attente du démarrage du serveur...")
    time.sleep(3)
    
    try:
        # Test de la page d'accueil
        response = requests.get('http://localhost:5000', timeout=5)
        if response.status_code == 200:
            print("✅ Page d'accueil accessible")
        else:
            print(f"❌ Erreur page d'accueil: {response.status_code}")
            return False
            
        # Test d'analyse avec une URL simple
        test_url = "http://example.com"
        print(f"🔍 Test d'analyse avec: {test_url}")
        
        analysis_response = requests.post(
            'http://localhost:5000/analyze',
            json={'url': test_url},
            timeout=30
        )
        
        if analysis_response.status_code == 200:
            result = analysis_response.json()
            print("✅ Analyse réussie!")
            print(f"📊 Score global: {result.get('scores', {}).get('overall', 'N/A')}")
            print(f"🔗 URL analysée: {result.get('url', 'N/A')}")
            return True
        else:
            print(f"❌ Erreur lors de l'analyse: {analysis_response.status_code}")
            print(f"📝 Réponse: {analysis_response.text}")
            return False
            
    except requests.exceptions.ConnectionError:
        print("❌ Impossible de se connecter au serveur")
        print("💡 Vérifiez que l'application est démarrée sur http://localhost:5000")
        return False
    except requests.exceptions.Timeout:
        print("❌ Timeout lors du test")
        return False
    except Exception as e:
        print(f"❌ Erreur inattendue: {e}")
        return False

if __name__ == '__main__':
    success = test_application()
    if success:
        print("\n🎉 Tous les tests sont passés!")
        print("🌐 L'application est prête à être utilisée sur http://localhost:5000")
    else:
        print("\n💥 Certains tests ont échoué")
        print("🔧 Vérifiez les logs du serveur pour plus de détails") 