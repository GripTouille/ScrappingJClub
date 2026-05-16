from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import os
import time

from fonctions import attendre_fin_telechargements

# --- CONFIGURATION DE BASE ---
# Ton dossier principal
BASE_TARGET_DIR = os.path.join(os.path.expanduser("~"), "Documents", "documents_prepa")
if not os.path.exists(BASE_TARGET_DIR):
    os.makedirs(BASE_TARGET_DIR)

options = webdriver.ChromeOptions()
prefs = {
    "download.prompt_for_download": False,
    "directory_upgrade": True,
    "plugins.always_open_pdf_externally": True 
}
options.add_experimental_option("prefs", prefs)

print("🚀 Lancement du navigateur...")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

try:
    # On ouvre le site
    driver.get("https://cahier-de-prepa.fr/mpsi2-charlemagne/")
    
    print("\n--- 🔐 ÉTAPE 1 : CONNEXION ---")
    print("Connecte-toi sur le site dans la fenêtre qui vient de s'ouvrir.")
    input("👉 Une fois connecté (sur n'importe quelle page), appuie sur ENTRÉE ici...")

    # On entre dans la boucle infinie
    while True:
        print("\n==================================================")
        print("🔄 PRÊT POUR UNE NOUVELLE ASPIRATION")
        print("==================================================")
        print("1. Dans ton navigateur, va dans la section voulue (ex: Cours, TD, DM...).")
        print("2. Reviens dans ce terminal.")
        
        # On demande le nom du dossier à l'utilisateur
        reponse = input("\n📂 Donne un nom pour le dossier de cette page (ou tape 'FIN' pour quitter) : ").strip()
        
        # Condition de sortie
        if reponse.upper() == 'FIN' or reponse == '':
            print("\n👋 Fin du programme. Bonnes révisions !")
            break
            
        # Création du sous-dossier spécifique (ex: documents_prepa/Cours)
        current_folder_path = os.path.join(BASE_TARGET_DIR, reponse)
        if not os.path.exists(current_folder_path):
            os.makedirs(current_folder_path)
            
        # CONFIGURATION DYNAMIQUE : On change le dossier de téléchargement à la volée !
        driver.execute_cdp_cmd("Browser.setDownloadBehavior", {
            "behavior": "allow",
            "downloadPath": os.path.abspath(current_folder_path)
        })

        # Scan des liens sur la page actuelle
        print("🔎 Analyse des documents sur la page...")
        all_links = driver.find_elements(By.TAG_NAME, "a")
        download_urls = []

        for link in all_links:
            href = link.get_attribute("href")
            if href and "download?id=" in href:
                download_urls.append(href)

        if not download_urls:
            print("❌ Aucun document téléchargeable trouvé sur cette page. Es-tu au bon endroit ?")
            continue
            
        print(f"✅ {len(download_urls)} fichiers détectés pour le dossier '{reponse}'.")
        print("📥 Téléchargement en cours...")

        for i, url in enumerate(download_urls):
            print(f"   [{i+1}/{len(download_urls)}] En cours...")
            driver.get(url) 
            
            attendre_fin_telechargements(current_folder_path)

        print(f"🎉 Terminé pour la section '{reponse}' !")
        print(f"📁 Tes fichiers sont rangés ici : {current_folder_path}")

finally:
    print("\nFermeture du navigateur...")
    driver.quit()