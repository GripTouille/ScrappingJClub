#!/bin/bash
# Forcer le Terminal à se placer dans le dossier du script
cd "$(dirname "$0")"

echo "=================================================="
echo " 🛠️  INSTALLATION DES DÉPENDANCES (MACOS) "
echo "=================================================="

# Vérifier si Python 3 est installé
if ! command -v python3 &> /dev/null
then
    echo "❌ Erreur : Python 3 n'est pas installé sur ce Mac."
    echo "Veuillez l'installer via https://www.python.org/downloads/ ou via Homebrew."
    exit 1
fi

echo "📦 Création de l'environnement virtuel (venv)..."
python3 -m venv venv

echo "🔌 Activation de l'environnement virtuel..."
source venv/bin/activate

echo "🔄 Mise à jour de pip..."
pip install --upgrade pip

echo "📥 Installation des modules requis (Selenium, Tkinter, etc.)..."
pip install -r requirements.txt

echo "=================================================="
echo " 🎉 Installation terminée avec succès ! "
echo " Vous pouvez maintenant fermer cette fenêtre. "
echo "=================================================="
