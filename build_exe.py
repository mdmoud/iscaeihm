#!/usr/bin/env python3
"""
Script pour créer un exécutable Windows de l'Analyseur Ergonomique
"""

import os
import subprocess
import sys

def build_exe():
    """Crée un exécutable Windows avec PyInstaller"""
    print("🔨 Création de l'exécutable Windows...")
    
    # Vérifier si PyInstaller est installé
    try:
        import PyInstaller
        print("✅ PyInstaller est installé")
    except ImportError:
        print("📦 Installation de PyInstaller...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller"])
    
    # Créer le fichier spec pour PyInstaller
    spec_content = """
# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['run.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('templates', 'templates'),
        ('README.md', '.'),
        ('INSTALLATION.md', '.'),
        ('examples.md', '.'),
    ],
    hiddenimports=[
        'flask',
        'requests',
        'selenium',
        'bs4',
        'webdriver_manager',
        'datetime',
        'time',
        'json',
        're'
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='AnalyseurErgonomique',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=None
)
"""
    
    with open('AnalyseurErgonomique.spec', 'w', encoding='utf-8') as f:
        f.write(spec_content)
    
    # Construire l'exécutable
    print("🔨 Construction de l'exécutable...")
    subprocess.check_call([
        sys.executable, "-m", "PyInstaller",
        "--clean",
        "AnalyseurErgonomique.spec"
    ])
    
    print("\n🎉 Exécutable créé avec succès!")
    print("📁 Fichier: dist/AnalyseurErgonomique.exe")
    print("\n📋 Instructions pour le destinataire:")
    print("1. Téléchargez et décompressez le fichier")
    print("2. Double-cliquez sur AnalyseurErgonomique.exe")
    print("3. L'application se lancera automatiquement")
    print("4. Ouvrez http://localhost:5000 dans le navigateur")

if __name__ == '__main__':
    build_exe() 