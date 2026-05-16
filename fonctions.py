import time
import os

def attendre_fin_telechargements(dossier):
    print("⏳ Attente de la fin du téléchargement...", end="", flush=True)
    while any(f.endswith(".crdownload") for f in os.listdir(dossier)):
        time.sleep(0.5)
        print(".", end="", flush=True)
    print(" OK !")