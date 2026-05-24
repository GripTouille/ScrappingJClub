@echo off
chcp 65001 > nul
title ScrappingJClub - Installateur de dépendances

echo ==================================================
echo 🚀 Installation des dépendances pour ScrappingJClub
echo ==================================================
echo.
echo ⏳ Patientez pendant que pip installe les modules requis...
echo.

python -m pip install --upgrade pip
python -m pip install -r requirements.txt

echo.
if %errorlevel% neq 0 (
    echo ❌ Une erreur est survenue lors de l'installation.
    echo 🤔 Vérifie que tu as bien coché la case "Add python.exe to PATH" lors de l'installation de Python.
) else (
    echo ✅ Installation terminée avec succès !
    echo 💡 Tu peux maintenant fermer cette fenêtre et double-cliquer sur 'lancer.bat'.
)
echo.
pause