from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time
import tkinter as tk
from tkinter import filedialog

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

print("🚀 Lancement du navigateur...")
# Utilisation du driver natif de Selenium 4 (plus stable, évite la page blanche data:,)
driver = webdriver.Chrome(options=options)

try:
    driver.get("https://cahier-de-prepa.fr/mpsi2-charlemagne/")
    
    print("\n--- 🔐 ÉTAPE 1 : CONNEXION ---")
    print("Connecte-toi sur le site dans la fenêtre qui vient de s'ouvrir.")
    input("👉 Une fois connecté, appuie sur ENTRÉE ici...")

    while True:
        print("\n==================================================")
        print("🔄 PRÊT POUR UNE NOUVELLE ASPIRATION")
        print("==================================================")
        print("1️⃣ Retourne sur Chrome.")
        print("2️⃣ Clique sur le dossier que tu veux aspirer (ex: Mathématiques > DM).")
        print("3️⃣ Reviens sur cette console.")
        
        choix = input("\n👉 C'est bon ? Appuie sur ENTRÉE pour choisir où sauvegarder (ou tape 'FIN' pour quitter) : ").strip()
        
        if choix.upper() == 'FIN':
            print("\n👋 Fin du programme. Bonnes révisions !")
            break
            
        print("📁 Ouvre la fenêtre de sélection (regarde dans ta barre des tâches si elle est cachée)...")
        
        # Initialiser l'interface graphique invisible pour l'explorateur Windows
        root = tk.Tk()
        root.withdraw() 
        root.attributes('-topmost', True) 

        # Ouvrir l'explorateur Windows
        current_folder_path = filedialog.askdirectory(
            title="Choisis où sauvegarder les fichiers de cette page",
            initialdir=BASE_TARGET_DIR
        )
        
        # Nettoyage de la fenêtre fantôme
        root.destroy()

        # Si l'utilisateur clique sur "Annuler" ou ferme la fenêtre
        if not current_folder_path:
            print("❌ Sélection annulée. On recommence.")
            continue
            
        print(f"📂 Destination choisie : {current_folder_path}")
            
        # Dire à Chrome de télécharger dans ce dossier précis
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
            
            # LE FILTRE ANTI-DOUBLON EST ICI 
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

        print(f"\n🎉 Session terminée pour ce dossier !")
        if fichiers_skappes > 0:
            print(f"ℹ️ Économie d'énergie : {fichiers_skappes} anciens fichiers ont été ignorés.")

finally:
    print("\nFermeture du navigateur...")
    driver.quit()