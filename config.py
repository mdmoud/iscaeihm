import os

class Config:
    """Configuration de base de l'application"""
    
    # Configuration Flask
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key-change-in-production'
    DEBUG = os.environ.get('FLASK_DEBUG', 'True').lower() == 'true'
    
    # Configuration Selenium
    SELENIUM_TIMEOUT = 10  # Timeout en secondes pour le chargement des pages
    SELENIUM_WINDOW_SIZE = (1920, 1080)  # Taille de la fenêtre du navigateur
    
    # Configuration de l'analyse
    MAX_ANALYSIS_TIME = 30  # Temps maximum d'analyse en secondes
    MIN_SCORE = 0
    MAX_SCORE = 100
    
    # Configuration des scores
    SCORE_WEIGHTS = {
        'usability': 0.3,
        'accessibility': 0.25,
        'design': 0.25,
        'navigation': 0.2
    }
    
    # Seuils pour les recommandations
    RECOMMENDATION_THRESHOLDS = {
        'low_score': 50,
        'medium_score': 75,
        'high_score': 90
    }
    
    # Configuration des composants WIMP
    WIMP_COMPONENTS = {
        'windows': ['modal', 'dialog', 'popup', 'overlay'],
        'icons': ['icon', 'svg', 'img'],
        'menus': ['nav', 'menu', 'dropdown', 'tabs'],
        'pointers': ['button', 'link', 'clickable']
    }

class DevelopmentConfig(Config):
    """Configuration pour le développement"""
    DEBUG = True
    SELENIUM_TIMEOUT = 15

class ProductionConfig(Config):
    """Configuration pour la production"""
    DEBUG = False
    SELENIUM_TIMEOUT = 5

class TestingConfig(Config):
    """Configuration pour les tests"""
    TESTING = True
    SELENIUM_TIMEOUT = 3

# Dictionnaire des configurations
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
} 