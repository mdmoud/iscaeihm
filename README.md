# Analyseur Ergonomique - Évaluation Automatique d'Interfaces

## Description

Cette application web analyse automatiquement l'ergonomie d'un site web en se basant sur les principes WIMP (Window, Icon, Menu, Pointer) et les bonnes pratiques de conception d'interfaces utilisateur.

## Fonctionnalités

- **Analyse complète** : Évaluation automatique des composants d'interface
- **Scores ergonomiques** : Calcul de scores pour différents aspects (facilité d'utilisation, accessibilité, design, navigation)
- **Rapport détaillé** : Génération d'un rapport complet avec recommandations
- **Interface moderne** : Design responsive et intuitif
- **Export de données** : Possibilité d'exporter les résultats

## Composants Analysés

### Principes WIMP
- **Window** : Fenêtres, modales, boîtes de dialogue
- **Icon** : Icônes, étiquettes, éléments visuels
- **Menu** : Menus de navigation, contextuels, onglets
- **Pointer** : Interactions de pointeur, éléments cliquables

### Éléments d'Interface
- Boutons (primaire, secondaire, avec icônes)
- Formulaires (champs, labels, validation)
- Navigation (liens internes/externes, recherche)
- Composants interactifs

## Installation

### Prérequis
- Python 3.8 ou supérieur
- Chrome ou Chromium (pour Selenium)
- pip (gestionnaire de paquets Python)

### Étapes d'installation

1. **Cloner ou télécharger le projet**
   ```bash
   git clone <url-du-repo>
   cd ErgoAutoEvaluation
   ```

2. **Créer un environnement virtuel (recommandé)**
   ```bash
   python -m venv venv
   
   # Sur Windows
   venv\Scripts\activate
   
   # Sur macOS/Linux
   source venv/bin/activate
   ```

3. **Installer les dépendances**
   ```bash
   pip install -r requirements.txt
   ```

## Utilisation

### Démarrage de l'application

1. **Lancer le serveur**
   ```bash
   python app.py
   ```

2. **Ouvrir le navigateur**
   - Aller à `http://localhost:5000`
   - L'interface web s'affichera

### Analyse d'un site web

1. **Entrer l'URL**
   - Saisir l'URL du site à analyser dans le champ de saisie
   - Exemples : `google.com`, `https://github.com`, `www.example.com`

2. **Lancer l'analyse**
   - Cliquer sur le bouton "Analyser"
   - Attendre le chargement (peut prendre quelques secondes)

3. **Consulter les résultats**
   - Scores ergonomiques globaux et par catégorie
   - Détail des composants analysés
   - Recommandations d'amélioration

4. **Exporter le rapport** (optionnel)
   - Cliquer sur "Exporter le Rapport"
   - Le fichier JSON sera téléchargé

## Structure du Projet

```
ErgoAutoEvaluation/
├── app.py                 # Application Flask principale
├── requirements.txt       # Dépendances Python
├── templates/
│   └── index.html        # Interface utilisateur
└── README.md             # Documentation
```

## Technologies Utilisées

- **Backend** : Python, Flask
- **Analyse Web** : Selenium, BeautifulSoup
- **Frontend** : HTML5, CSS3, JavaScript
- **Interface** : Font Awesome (icônes)

## Critères d'Évaluation

### Score de Facilité d'Utilisation
- Nombre d'éléments interactifs
- Ratio labels/champs de formulaire
- Clarté des boutons et liens

### Score d'Accessibilité
- Éléments focusables
- Présence de breadcrumbs
- Fonction de recherche

### Score de Design
- Utilisation d'icônes
- Organisation en onglets
- Éléments visuels

### Score de Navigation
- Liens internes
- Structure de navigation
- Hiérarchie des pages

## Exemple de Rapport

```
Rapport Ergonomique pour https://example.com
Date de l'analyse : 2024-01-15 14:30:25

Score Global : 75/100

Scores par catégorie :
- Facilité d'Utilisation : 80/100
- Accessibilité : 70/100
- Design : 75/100
- Navigation : 75/100

Composants analysés :
- 15 boutons
- 8 formulaires
- 25 liens
- 12 icônes
- 3 menus de navigation

Recommandations :
✓ Ajouter des breadcrumbs pour améliorer la navigation
✓ Améliorer l'accessibilité en ajoutant des éléments focusables
```

## Dépannage

### Problèmes courants

1. **Erreur de driver Chrome**
   - Vérifier que Chrome est installé
   - Le driver sera téléchargé automatiquement

2. **Timeout lors de l'analyse**
   - Vérifier la connexion internet
   - Certains sites peuvent être lents à charger

3. **Erreur de port**
   - Changer le port dans `app.py` si le port 5000 est occupé

### Logs et débogage

L'application affiche des messages d'erreur détaillés en cas de problème. Vérifiez la console pour plus d'informations.

## Contribution

Les contributions sont les bienvenues ! N'hésitez pas à :
- Signaler des bugs
- Proposer des améliorations
- Ajouter de nouveaux critères d'évaluation

## Licence

Ce projet est sous licence MIT. Voir le fichier LICENSE pour plus de détails.

## Support

Pour toute question ou problème, veuillez ouvrir une issue sur le repository du projet. 