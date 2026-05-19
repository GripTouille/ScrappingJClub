@echo off
chcp 65001 > nul
title ScrappingJClub - Console de Scraping

echo ==================================================
echo 🎯 Lancement de ScrappingJClub
echo ==================================================
echo.

python scrapp.py

echo.
if %errorlevel% neq 0 (
    echo ❌ Le script s'est arrêté de manière inattendue.
    echo 🤔 Si le message dit que 'python' n'est pas reconnu, c'est que Python n'est pas dans le PATH de ton PC.
)
echo.
pause