#!/bin/bash
# Forcer le Terminal à se placer dans le dossier du script
cd "$(dirname "$0")"

echo "=================================================="
echo " 🚀  LANCEMENT DE SCRAPPINGJCLUB (MACOS) "
echo "=================================================="

# Vérifier si le venv existe
if [ ! -d "venv" ]; then
    echo "❌ L'environnement virtuel n'existe pas."
    echo "Veuillez d'abord double-cliquer sur 'installer_mac.command'."
    exit 1
fi

echo "🔌 Activation de l'environnement virtuel..."
source venv/bin/activate

echo "🐍 Exécution du script Python..."
python3 scrapp.py

echo "=================================================="
echo " 🚪  Fermeture du navigateur et fin du programme."
echo "=================================================="
