@echo off
echo ========================================
echo   Analyseur Ergonomique - Demarrage
echo ========================================
echo.

REM Vérifier si Python est installé
python --version >nul 2>&1
if errorlevel 1 (
    echo ERREUR: Python n'est pas installé ou n'est pas dans le PATH
    echo Veuillez installer Python depuis https://python.org
    pause
    exit /b 1
)

echo Python detecte: 
python --version
echo.

REM Vérifier si les dépendances sont installées
echo Verification des dependances...
python -c "import flask, requests, selenium, bs4" >nul 2>&1
if errorlevel 1 (
    echo Installation des dependances...
    pip install Flask requests beautifulsoup4 selenium webdriver-manager
    if errorlevel 1 (
        echo ERREUR: Impossible d'installer les dependances
        pause
        exit /b 1
    )
)

echo.
echo ========================================
echo   Demarrage du serveur...
echo ========================================
echo.
echo L'application sera accessible sur:
echo http://localhost:5000
echo.
echo Pour arreter le serveur, fermez cette fenetre
echo ou appuyez sur Ctrl+C
echo.
echo ========================================
echo.

REM Démarrer l'application
python run.py

pause 