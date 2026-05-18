from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import os
import time

from fonctions import (
    attendre_fin_telechargements, 
    verifier_si_deja_telecharge, 
    enregistrer_dans_historique
)

# --- CONFIGURATION DE BASE ---
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

def main():
    print("🚀 Lancement du navigateur...")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    try:
        driver.get("https://cahier-de-prepa.fr/mpsi2-charlemagne/")

        print("\n--- 🔐 ÉTAPE 1 : CONNEXION ---")
        print("Connecte-toi sur le site dans la fenêtre qui vient de s'ouvrir.")
        input("👉 Une fois connecté, appuie sur ENTRÉE ici...")

        while True:
            print("\n==================================================")
            print("🔄 PRÊT POUR UNE NOUVELLE ASPIRATION")
            print("==================================================")

            reponse = input("\n📂 Nom du dossier pour cette page (ou 'FIN' pour quitter) : ").strip()

            if reponse.upper() == 'FIN' or reponse == '':
                print("\n👋 Fin du programme. Bonnes révisions !")
                break

            current_folder_path = os.path.join(BASE_TARGET_DIR, reponse)
            if not os.path.exists(current_folder_path):
                os.makedirs(current_folder_path)

            driver.execute_cdp_cmd("Browser.setDownloadBehavior", {
                "behavior": "allow",
                "downloadPath": os.path.abspath(current_folder_path)
            })

            print("🔎 Analyse des documents...")
            all_links = driver.find_elements(By.TAG_NAME, "a")
            download_urls = []

            for link in all_links:
                href = link.get_attribute("href")
                if href and "download?id=" in href:
                    download_urls.append(href)

            if not download_urls:
                print("❌ Aucun document trouvé sur cette page.")
                continue

            print(f"✅ {len(download_urls)} fichiers détectés.")

            # Lancement des téléchargements avec anti-doublon
            fichiers_skappes = 0
            for i, url in enumerate(download_urls):
                # Extraire l'ID unique du fichier depuis l'URL
                file_id = url.split("id=")[-1].split("&")[0]

                #  LE FILTRE ANTI-DOUBLON EST ICI 
                if verifier_si_deja_telecharge(current_folder_path, file_id):
                    print(f"   [{i+1}/{len(download_urls)}] ⏭️ Déjà synchronisé (ID: {file_id}) -> Ignoré.")
                    fichiers_skappes += 1
                    continue

                print(f"   [{i+1}/{len(download_urls)}] 📥 Nouveau fichier détecté ! Lancement...")
                driver.get(url) 

                # Attente de la fin du téléchargement Chrome
                attendre_fin_telechargements(current_folder_path)

                # On l'inscrit dans l'historique pour la prochaine fois
                enregistrer_dans_historique(current_folder_path, file_id)

            print(f"\n🎉 Session terminée pour '{reponse}' !")
            if fichiers_skappes > 0:
                print(f"ℹ️ Économie d'énergie : {fichiers_skappes} anciens fichiers ont été ignorés.")

    finally:
        print("\nFermeture du navigateur...")
        driver.quit()
if __name__ == "__main__":
    main()