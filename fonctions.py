import os
import time

def attendre_fin_telechargements(dossier):
    """ Bloque le script tant que Chrome n'a pas fini de télécharger les fichiers """
    time.sleep(0.3)
    print("⏳ Téléchargement en cours...", end="", flush=True)
    while any(f.endswith(".crdownload") for f in os.listdir(dossier)):
        time.sleep(0.5)
        print(".", end="", flush=True)
    print(" ✅ Terminé !")

def verifier_si_deja_telecharge(dossier, file_id):
    """ Regarde dans le fichier historique si cet ID a déjà été récupéré """
    fichier_histoire = os.path.join(dossier, "historique_sync.txt")
    
    # Si le fichier d'historique n'existe pas encore, c'est que le dossier est neuf
    if not os.path.exists(fichier_histoire):
        return False
        
    with open(fichier_histoire, "r", encoding="utf-8") as f:
        ids_sauvegardes = f.read().splitlines()
        
    return str(file_id) in ids_sauvegardes

def enregistrer_dans_historique(dossier, file_id):
    """ Ajoute l'ID du fichier dans le journal du dossier """
    fichier_histoire = os.path.join(dossier, "historique_sync.txt")
    with open(fichier_histoire, "a", encoding="utf-8") as f:
        f.write(f"{file_id}\n")