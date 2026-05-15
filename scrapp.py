from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import os
import time

# --- CONFIGURATION ---
# Utilise le chemin complet pour être sûr
TARGET_DIR = os.path.join(os.path.expanduser("~"), "Documents", "documents_prepa")
if not os.path.exists(TARGET_DIR):
    os.makedirs(TARGET_DIR)

# CONFIGURATION SPÉCIALE POUR LE TÉLÉCHARGEMENT AUTOMATIQUE
options = webdriver.ChromeOptions()
prefs = {
    "download.default_directory": TARGET_DIR, # Dossier où les PDF vont tomber
    "download.prompt_for_download": False,    # Ne pas demander de confirmation
    "directory_upgrade": True,
    "plugins.always_open_pdf_externally": True # Force le téléchargement au lieu d'ouvrir le lecteur
}
options.add_experimental_option("prefs", prefs)

print("🚀 Lancement du navigateur...")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

try:
    driver.get("https://cahier-de-prepa.fr/mpsi2-charlemagne/")
    
    print("\n--- 📝 ACTION ---")
    print(f"1. Connecte-toi et va sur ta page de cours.")
    print(f"2. Tes fichiers seront enregistrés ici : {TARGET_DIR}")
    input("👉 Une fois la liste des chapitres affichée, appuie sur ENTRÉE...")

    # On cherche les liens de téléchargement
    print("🔎 Analyse de la page...")
    all_links = driver.find_elements(By.TAG_NAME, "a")
    download_urls = []

    for link in all_links:
        href = link.get_attribute("href")
        if href and "download?id=" in href:
            download_urls.append(href)

    if not download_urls:
        print("❌ Aucun lien trouvé !")
    else:
        print(f"✅ {len(download_urls)} fichiers détectés. Lancement du téléchargement natif...")

        for i, url in enumerate(download_urls):
            print(f"[{i+1}/{len(download_urls)}] 📥 Récupération...")
            # On navigue directement sur l'URL de téléchargement
            # Grâce aux options 'prefs' plus haut, le navigateur va le télécharger direct
            driver.get(url) 
            time.sleep(1) # Petit délai pour laisser le téléchargement démarrer

    print(f"\n✨ TERMINÉ ! Vérifie ton dossier '{TARGET_DIR}'.")
    print("Les fichiers devraient maintenant faire plusieurs centaines de Ko.")

finally:
    print("\nFermeture dans 10 secondes...")
    time.sleep(10)
    driver.quit()