# 🚀 ScrappingJClub

> **Ferfoui is the goat, don't forget.** 🐐
> *This repository is meant to scrap Cahier de Prépa's folders as if you were a true J club member!*

`ScrappingJClub` est un outil de synchronisation automatique et intelligent conçu pour aspirer proprement les documents (Cours, TD, DM) depuis la plateforme *Cahier de Prépa*. Grâce à son architecture modulaire et son pilotage de navigateur, il contourne les protections de session et classe tout automatiquement sur votre ordinateur.

---

## ✨ Fonctionnalités

* **Aspiration Infinie en Boucle :** Pas besoin de relancer le script pour chaque matière. Vous naviguez, vous nommez le dossier, le script s'occupe du reste.
* **Téléchargement Natif Sécurisé :** Utilise le navigateur lui-même pour télécharger les fichiers, évitant ainsi les blocages de sécurité et les fichiers corrompus de 5 Ko.
* **Gestionnaire Anti-Coupure :** Le script surveille l'état des téléchargements et attend patiemment la fin de chaque fichier avant de passer au suivant.
* **Filtre Anti-Doublon :** Un système d'historique intelligent évite de retélécharger les documents que vous possédez déjà.

---

## 🛠️ Installation & Utilisation (Guide Rapide)

Pas besoin d'être un expert en informatique, suis juste ces 3 étapes :

### Étape 1 : Installer Python et Google Chrome
1. Télécharge et installe **Google Chrome** (si ce n'est pas déjà fait).
2. Télécharge **Python 3.x** sur le site officiel.
3. ⚠️ **TRÈS IMPORTANT lors de l'installation de Python :** Coche bien la case **"Add python.exe to PATH"** tout en bas de la première fenêtre avant de cliquer sur "Install Now". Si tu oublies, le script ne pourra pas se lancer.

### Étape 2 : Récupérer le projet
1. Clique sur le bouton vert **`Code`** en haut à droite de cette page GitHub, puis sur **`Download ZIP`**.
2. Extrais le fichier ZIP là où tu veux sur ton ordinateur (par exemple dans tes Documents).

### Étape 3 : Installer et Lancer !
  **Sous Windows :**
  1. Double-clique sur `installer.bat` (attends que la fenêtre te dise que c'est fini).
  2. Double-clique sur `lancer.bat` pour démarrer le script !
  
  **Sous Mac / Linux (via le Terminal) :**
  1. Ouvre ton terminal dans le dossier et tape : `pip install -r requirements.txt`
  2. Lance le script avec : `python scrapp.py`

---

## 📖 Comment ça marche une fois lancé ?
1. Une fenêtre Google Chrome va s'ouvrir toute seule.
2. Connecte-toi manuellement à ton compte *Cahier de Prépa*.
3. Reviens sur la console (la fenêtre noire) et appuie sur **ENTRÉE**.
4. Entre le nom que tu veux donner au dossier (ex: `Physique_TD` ou `Maths_Cours`).
5. Laisse la magie opérer ! Les fichiers seront classés proprement dans ton dossier `Documents/documents_prepa/`.

