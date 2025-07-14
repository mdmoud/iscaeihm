from flask import Flask, render_template, request, jsonify
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
from datetime import datetime
import re
import json

app = Flask(__name__)

def setup_driver():
    """Configure le driver Selenium pour l'analyse"""
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--window-size=1920,1080")
    
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    return driver

def analyze_ergonomics(url):
    """Analyse ergonomique complète d'un site web"""
    driver = None
    try:
        # Vérification de l'URL
        if not url or not url.strip():
            return {
                'error': 'URL invalide ou vide',
                'url': url,
                'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
        
        # Récupération du contenu HTML avec gestion d'erreur spécifique
        try:
            response = requests.get(url, timeout=15, allow_redirects=True)
            response.raise_for_status()  # Lève une exception pour les codes d'erreur HTTP
        except requests.exceptions.ConnectionError:
            return {
                'error': f'Impossible de se connecter au site {url}. Vérifiez que l\'URL est correcte et que le site est accessible.',
                'url': url,
                'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
        except requests.exceptions.Timeout:
            return {
                'error': f'Le site {url} met trop de temps à répondre. Vérifiez que le site est accessible.',
                'url': url,
                'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
        except requests.exceptions.HTTPError as e:
            if e.response.status_code == 404:
                return {
                    'error': f'Le site {url} n\'existe pas (erreur 404). Vérifiez l\'URL.',
                    'url': url,
                    'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                }
            else:
                return {
                    'error': f'Erreur HTTP {e.response.status_code} pour {url}. Le site n\'est pas accessible.',
                    'url': url,
                    'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                }
        except requests.exceptions.RequestException as e:
            return {
                'error': f'Erreur de requête pour {url}: {str(e)}',
                'url': url,
                'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
        
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Analyse avec Selenium pour les éléments dynamiques
        try:
            driver = setup_driver()
            driver.get(url)
            time.sleep(3)  # Attendre le chargement
        except Exception as e:
            if driver:
                driver.quit()
            return {
                'error': f'Erreur lors du chargement de la page avec Selenium: {str(e)}',
                'url': url,
                'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
        
        # Collecte des données
        analysis_data = {
            'url': url,
            'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'components': {},
            'scores': {},
            'recommendations': {}
        }
        
        # Analyse des composants WIMP
        analysis_data['components'] = analyze_wimp_components(driver, soup)
        
        # Calcul des scores
        analysis_data['scores'] = calculate_scores(analysis_data['components'])
        
        # Génération des recommandations
        analysis_data['recommendations'] = generate_recommendations(analysis_data['components'], analysis_data['scores'])
        
        if driver:
            driver.quit()
        return analysis_data
        
    except Exception as e:
        if driver:
            driver.quit()
        return {
            'error': f'Erreur inattendue lors de l\'analyse: {str(e)}',
            'url': url,
            'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

def analyze_wimp_components(driver, soup):
    """Analyse les composants WIMP (Window, Icon, Menu, Pointer)"""
    components = {
        'windows': analyze_windows(driver, soup),
        'icons': analyze_icons(driver, soup),
        'menus': analyze_menus(driver, soup),
        'pointers': analyze_pointers(driver, soup),
        'buttons': analyze_buttons(driver, soup),
        'forms': analyze_forms(driver, soup),
        'navigation': analyze_navigation(driver, soup)
    }
    return components

def analyze_windows(driver, soup):
    """Analyse les fenêtres et modales"""
    windows = {
        'modals': len(driver.find_elements(By.CSS_SELECTOR, '[role="dialog"], .modal, .popup')),
        'dialogs': len(driver.find_elements(By.CSS_SELECTOR, 'dialog, [role="dialog"]')),
        'popups': len(driver.find_elements(By.CSS_SELECTOR, '.popup, .tooltip')),
        'overlays': len(driver.find_elements(By.CSS_SELECTOR, '.overlay, .backdrop'))
    }
    return windows

def analyze_icons(driver, soup):
    """Analyse les icônes"""
    icons = {
        'total': len(driver.find_elements(By.CSS_SELECTOR, 'i, .icon, [class*="icon"], svg')),
        'svg': len(driver.find_elements(By.CSS_SELECTOR, 'svg')),
        'font_icons': len(driver.find_elements(By.CSS_SELECTOR, 'i, [class*="fa-"], [class*="icon-"]')),
        'images': len(driver.find_elements(By.CSS_SELECTOR, 'img[src*="icon"], img[alt*="icon"]'))
    }
    return icons

def analyze_menus(driver, soup):
    """Analyse les menus"""
    menus = {
        'navigation': len(driver.find_elements(By.CSS_SELECTOR, 'nav, .nav, .navigation, .menu')),
        'dropdown': len(driver.find_elements(By.CSS_SELECTOR, '.dropdown, .select, select')),
        'contextual': len(driver.find_elements(By.CSS_SELECTOR, '[contextmenu], .context-menu')),
        'tabs': len(driver.find_elements(By.CSS_SELECTOR, '.tabs, .tab, [role="tab"]')),
        'breadcrumbs': len(driver.find_elements(By.CSS_SELECTOR, '.breadcrumb, .breadcrumbs'))
    }
    return menus

def analyze_pointers(driver, soup):
    """Analyse les interactions de pointeur"""
    pointers = {
        'clickable': len(driver.find_elements(By.CSS_SELECTOR, 'a, button, [onclick], [role="button"]')),
        'hoverable': len(driver.find_elements(By.CSS_SELECTOR, '[title], [data-tooltip], .tooltip')),
        'draggable': len(driver.find_elements(By.CSS_SELECTOR, '[draggable="true"], .draggable')),
        'focusable': len(driver.find_elements(By.CSS_SELECTOR, 'input, button, a, [tabindex]'))
    }
    return pointers

def analyze_buttons(driver, soup):
    """Analyse les boutons"""
    buttons = {
        'total': len(driver.find_elements(By.CSS_SELECTOR, 'button, .btn, [role="button"]')),
        'primary': len(driver.find_elements(By.CSS_SELECTOR, '.btn-primary, .primary, [class*="primary"]')),
        'secondary': len(driver.find_elements(By.CSS_SELECTOR, '.btn-secondary, .secondary, [class*="secondary"]')),
        'disabled': len(driver.find_elements(By.CSS_SELECTOR, 'button[disabled], .btn[disabled]')),
        'with_icons': len(driver.find_elements(By.CSS_SELECTOR, 'button i, .btn i, button svg, .btn svg'))
    }
    return buttons

def analyze_forms(driver, soup):
    """Analyse les formulaires"""
    forms = {
        'total': len(driver.find_elements(By.CSS_SELECTOR, 'form')),
        'inputs': len(driver.find_elements(By.CSS_SELECTOR, 'input')),
        'text_areas': len(driver.find_elements(By.CSS_SELECTOR, 'textarea')),
        'selects': len(driver.find_elements(By.CSS_SELECTOR, 'select')),
        'checkboxes': len(driver.find_elements(By.CSS_SELECTOR, 'input[type="checkbox"]')),
        'radios': len(driver.find_elements(By.CSS_SELECTOR, 'input[type="radio"]')),
        'labels': len(driver.find_elements(By.CSS_SELECTOR, 'label'))
    }
    return forms

def analyze_navigation(driver, soup):
    """Analyse la navigation"""
    navigation = {
        'links': len(driver.find_elements(By.CSS_SELECTOR, 'a')),
        'internal_links': len(driver.find_elements(By.CSS_SELECTOR, 'a[href^="/"], a[href^="#"]')),
        'external_links': len(driver.find_elements(By.CSS_SELECTOR, 'a[href^="http"]')),
        'search': len(driver.find_elements(By.CSS_SELECTOR, 'input[type="search"], .search, #search')),
        'pagination': len(driver.find_elements(By.CSS_SELECTOR, '.pagination, .pager, [class*="page"]'))
    }
    return navigation

def calculate_scores(components):
    """Calcule les scores ergonomiques sur 10"""
    scores = {
        'lisibilite': 0.0,
        'coherence': 0.0,
        'feedback': 0.0,
        'overall': 0.0
    }
    
    # Score de lisibilité (sur 10)
    total_elements = (components['buttons']['total'] + 
                     components['navigation']['links'] + 
                     components['forms']['total'] + 
                     components['icons']['total'])
    
    if total_elements > 0:
        # Plus d'éléments = plus de complexité potentielle
        if total_elements < 20:
            scores['lisibilite'] = 8
        elif total_elements < 50:
            scores['lisibilite'] = 6
        else:
            scores['lisibilite'] = 4
    
    # Score de cohérence (sur 10)
    if components['buttons']['with_icons'] > 0:
        scores['coherence'] += 2
    
    if components['menus']['navigation'] > 0:
        scores['coherence'] += 2
    
    if components['forms']['labels'] >= components['forms']['inputs']:
        scores['coherence'] += 2
    
    if components['icons']['total'] > 0:
        scores['coherence'] += 2
    
    if components['navigation']['search'] > 0:
        scores['coherence'] += 1
    
    if components['menus']['breadcrumbs'] > 0:
        scores['coherence'] += 1
    
    # Limiter à 10
    scores['coherence'] = min(10, scores['coherence'])
    
    # Score de feedback utilisateur (sur 10)
    if components['pointers']['hoverable'] > 0:
        scores['feedback'] += 3
    
    if components['buttons']['total'] > 0:
        scores['feedback'] += 2
    
    if components['forms']['total'] > 0:
        scores['feedback'] += 2
    
    if components['menus']['dropdown'] > 0:
        scores['feedback'] += 2
    
    if components['windows']['modals'] > 0:
        scores['feedback'] += 1
    
    # Limiter à 10
    scores['feedback'] = min(10, scores['feedback'])
    
    # Score global (moyenne des 3 critères)
    scores['overall'] = (scores['lisibilite'] + scores['coherence'] + scores['feedback']) / 3
    
    return scores

def generate_recommendations(components, scores):
    """Génère des recommandations d'amélioration selon le nouveau format"""
    recommendations = {
        'lisibilite': {
            'status': 'OK' if scores['lisibilite'] >= 6 else 'Attention' if scores['lisibilite'] >= 4 else 'Manquant',
            'description': 'La lisibilité concerne la facilité avec laquelle l\'utilisateur peut lire et comprendre les informations affichées. Une bonne lisibilité implique des polices adaptées, des contrastes suffisants, et une organisation claire.',
            'conseil': 'Utilisez des polices lisibles, des tailles adaptées, et assurez un contraste suffisant entre le texte et le fond.'
        },
        'coherence': {
            'status': 'OK' if scores['coherence'] >= 6 else 'Attention' if scores['coherence'] >= 4 else 'Manquant',
            'description': 'La cohérence garantit que les éléments de l\'interface se comportent et se présentent de manière uniforme, facilitant l\'apprentissage et l\'utilisation.',
            'conseil': 'Respectez les conventions de design, harmonisez les couleurs, icônes et comportements des boutons/menus.'
        },
        'feedback': {
            'status': 'OK' if scores['feedback'] >= 6 else 'Attention' if scores['feedback'] >= 4 else 'Manquant',
            'description': 'Le feedback utilisateur désigne les réponses visuelles, sonores ou haptiques fournies après une action (clic, saisie, etc.), permettant à l\'utilisateur de comprendre l\'état du système.',
            'conseil': 'Ajoutez des messages, animations ou changements visuels pour signaler la prise en compte des actions de l\'utilisateur.'
        }
    }
    
    # Recommandations générales
    general_recommendations = []
    
    if scores['coherence'] < 6:
        general_recommendations.append(f"Améliorer le critère Cohérence : {recommendations['coherence']['conseil']}")
    
    if scores['feedback'] < 4:
        general_recommendations.append(f"Le critère Feedback utilisateur est manquant : {recommendations['feedback']['conseil']}")
    
    return {
        'details': recommendations,
        'general': general_recommendations
    }

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    url = data.get('url')
    
    if not url:
        return jsonify({'error': 'URL requise'}), 400
    
    # Ajouter http:// si nécessaire
    if not url.startswith(('http://', 'https://')):
        url = 'https://' + url
    
    analysis_result = analyze_ergonomics(url)
    return jsonify(analysis_result)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000) 