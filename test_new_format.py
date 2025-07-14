#!/usr/bin/env python3
"""
Test du nouveau format de rapport ergonomique
"""

import requests
import time
import json

def test_new_format():
    """Test du nouveau format de rapport"""
    print("🧪 Test du nouveau format de rapport...")
    
    # Attendre que le serveur démarre
    print("⏳ Attente du démarrage du serveur...")
    time.sleep(3)
    
    try:
        # Test avec une URL simple
        test_url = "http://example.com"
        print(f"🔍 Test d'analyse avec: {test_url}")
        
        response = requests.post(
            'http://localhost:5000/analyze',
            json={'url': test_url},
            timeout=30
        )
        
        if response.status_code == 200:
            result = response.json()
            print("✅ Analyse réussie!")
            
            # Vérifier le nouveau format
            print("\n📊 Vérification du nouveau format:")
            
            # Score global sur 10
            if 'scores' in result and 'overall' in result['scores']:
                score = result['scores']['overall']
                print(f"✅ Score global: {score}/10")
            
            # Nouveaux critères
            expected_criteria = ['lisibilite', 'coherence', 'feedback']
            for critere in expected_criteria:
                if critere in result['scores']:
                    print(f"✅ Critère {critere}: {result['scores'][critere]}/10")
                else:
                    print(f"❌ Critère {critere} manquant")
            
            # Recommandations détaillées
            if 'recommendations' in result and 'details' in result['recommendations']:
                print("✅ Recommandations détaillées présentes")
                for critere, details in result['recommendations']['details'].items():
                    print(f"  - {critere}: {details['status']}")
            else:
                print("❌ Recommandations détaillées manquantes")
            
            # Recommandations générales
            if 'recommendations' in result and 'general' in result['recommendations']:
                print(f"✅ Recommandations générales: {len(result['recommendations']['general'])} items")
            else:
                print("❌ Recommandations générales manquantes")
            
            return True
            
        else:
            print(f"❌ Erreur lors de l'analyse: {response.status_code}")
            print(f"📝 Réponse: {response.text}")
            return False
            
    except requests.exceptions.ConnectionError:
        print("❌ Impossible de se connecter au serveur")
        return False
    except Exception as e:
        print(f"❌ Erreur inattendue: {e}")
        return False

def print_sample_report():
    """Affiche un exemple de rapport attendu"""
    print("\n📋 Exemple de rapport attendu:")
    print("=" * 50)
    print("""
Rapport ergonomique pour example.com
Date de l'analyse : 13/07/2025 19:40

Résumé
Ce rapport analyse l'ergonomie de l'interface en s'appuyant sur les principaux composants graphiques et textuels, selon les principes WIMP (Window, Icon, Menu, Pointer) et les bonnes pratiques de conception.

Types d'interfaces
Textuelles : Permettent l'interaction via du texte (ex : ligne de commande, chat).
Graphiques : Objets dessinés à l'écran (pictogrammes, boutons, menus, fenêtres, etc.).

Principaux composants WIMP
Window : Fenêtres (modales, non modales, boîtes de dialogue, flottantes, pop-up, etc.)
Icon : Icônes, étiquettes
Menu : Menus de commande, contextuels, circulaires, onglets, rubans
Pointer : Pointeur de souris, interactions directes

Composants d'interface analysés
Boutons : Poussoir, case à cocher, bouton radio
Menus : Commande, contextuel, circulaire
Onglets, Rubans : Navigation et accès rapide aux fonctionnalités
Listes : Encombrement fort/faible, arborescentes
Zones de texte : Mono-ligne, multi-ligne, tableau, sélecteur de date, lien hypertexte
Multifenêtrage : Superposition (à éviter), mosaïque, hiérarchique, MDI

Score global : 6.5 / 10

Analyse détaillée des critères
Lisibilité: OK
La lisibilité concerne la facilité avec laquelle l'utilisateur peut lire et comprendre les informations affichées. Une bonne lisibilité implique des polices adaptées, des contrastes suffisants, et une organisation claire.
Conseil : Utilisez des polices lisibles, des tailles adaptées, et assurez un contraste suffisant entre le texte et le fond.

Cohérence: Attention
La cohérence garantit que les éléments de l'interface se comportent et se présentent de manière uniforme, facilitant l'apprentissage et l'utilisation.
Conseil : Respectez les conventions de design, harmonisez les couleurs, icônes et comportements des boutons/menus.

Feedback utilisateur: Manquant
Le feedback utilisateur désigne les réponses visuelles, sonores ou haptiques fournies après une action (clic, saisie, etc.), permettant à l'utilisateur de comprendre l'état du système.
Conseil : Ajoutez des messages, animations ou changements visuels pour signaler la prise en compte des actions de l'utilisateur.

Recommandations générales
Améliorer le critère Cohérence : Respectez les conventions de design, harmonisez les couleurs, icônes et comportements des boutons/menus.
Le critère Feedback utilisateur est manquant : Ajoutez des messages, animations ou changements visuels pour signaler la prise en compte des actions de l'utilisateur.

Aspects analysés
Aspect utilisateur : Facilité d'utilisation, accessibilité, satisfaction.
Aspect programmeur : Facilité de développement, modularité, maintenabilité.
Aspect concepteur : Respect des standards, innovation, adaptation au contexte d'usage.
""")
    print("=" * 50)

if __name__ == '__main__':
    print_sample_report()
    success = test_new_format()
    if success:
        print("\n🎉 Le nouveau format fonctionne correctement!")
        print("🌐 Testez l'interface sur http://localhost:5000")
    else:
        print("\n💥 Le test a échoué")
        print("🔧 Vérifiez les logs du serveur") 