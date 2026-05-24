# 🚀 ScrappingJClub — Aspirateur de Documents (Cahier de Prépa)

Bienvenue dans le projet **ScrappingJClub** ! Ce script d'automatisation en Python a été spécialement conçu pour simplifier la récupération, la sauvegarde et l'organisation des cours, TD, TP et DM depuis la plateforme **Cahier de Prépa** (spécifiquement configuré pour la classe **MPSI2 Charlemagne**). 

Grâce à des scripts d'automatisation cliquables pour Windows (`.bat`) et pour macOS (`.command`), l'installation et l'utilisation ont été simplifiées au maximum afin qu'aucune compétence technique ou manipulation complexe de terminal ne soit requise au quotidien.

---

## 📋 Table des Matières
1. [Fonctionnalités](#-fonctionnalités)
2. [Structure du Projet](#-structure-du-projet)
3. [Prérequis](#-prérequis)
4. [⚡ Configuration & Utilisation sous WINDOWS](#-configuration--utilisation-sous-windows)
5. [🍏 Configuration & Utilisation sous MACOS](#-configuration--utilisation-sous-macos)
6. [🔄 Guide d'Utilisation Général (Le Script)](#-guide-dutilisation-général-le-script)
7. [🔍 Dépannage & FAQ](#-dépannage--faq)
8. [Avertissement Légal](#-avertissement-légal)

---

## ✨ Fonctionnalités

* **Connexion Assistée :** Ouvre une instance sécurisée de votre navigateur pour vous laisser vous authentifier sereinement (gestion des identifiants par l'utilisateur).
* **Aspiration Sélective :** Vous permet de choisir précisément quel dossier (ex: *Mathématiques > DM*) vous souhaitez télécharger en local.
* **Sélection Graphique Native :** Intègre une boîte de dialogue masquée (`tkinter`) pour vous laisser choisir l'emplacement exact de sauvegarde (compatible Windows Explorer et Mac Finder).
* **Zéro Ligne de Commande au Quotidien :** Orchestration complète via des raccourcis cliquables adaptés à votre système d'exploitation.
* **Gestion Propre des Erreurs :** Fermeture automatique du navigateur en fin de processus pour ne pas saturer la mémoire de votre ordinateur.

---

## 📂 Structure du Projet

Voici l'architecture des fichiers présents dans votre dossier :

| Fichier / Dossier | Système | Description |
| :--- | :--- | :--- |
| `scrapp.py` | Universel | **Script principal**. Gère la boucle principale, la console en émojis, la navigation Selenium et l'interaction utilisateur. |
| `fonctions.py` | Universel | **Module utilitaire**. Regroupe les fonctions de téléchargement, de création de dossiers et d'analyse HTML. |
| `requirements.txt` | Universel | Liste des bibliothèques Python tierces indispensables (ex: `selenium`). |
| `installer.bat` | 🪟 Windows | Script d'installation automatique pour Windows (Double-clic). |
| `lancer.bat` | 🪟 Windows | Script de lancement automatique pour Windows (Double-clic). |
| `installer_mac.command`| 🍏 macOS | Script d'installation automatique pour Mac (Double-clic après autorisation). |
| `lancer_mac.command` | 🍏 macOS | Script de lancement automatique pour Mac (Double-clic). |
| `.gitignore` | Outil | Configuration excluant les fichiers temporaires et les caches (`__pycache__`). |
| `LICENSE` | Outil | Conditions d'utilisation et de distribution de ce projet. |

---

## 🛠️ Prérequis

Avant de démarrer, assurez-vous de disposer des éléments suivants :
1. **Un navigateur Google Chrome à jour** (indispensable pour l'automatisation Selenium).
2. [Python3](https://www.python.org/downloads/) installé sur votre machine :
   * **Windows :** Pensez à cocher l'option *"Add Python to PATH"* lors de l'installation.
   * **Mac :** Installez-le via le site officiel (python.org) ou via Homebrew (`brew install python`).

---

## ⚡ Configuration & Utilisation sous WINDOWS

### Première installation (Une seule fois)
1. Ouvrez le dossier du projet.
2. Double-cliquez sur le fichier **`installer.bat`**.
3. Une fenêtre noire va s'ouvrir, installer l'environnement et se fermer seule.

### Lancement quotidien
* Double-cliquez simplement sur **`lancer.bat`** pour démarrer le programme.
* Suivez ensuite le [Guide d'Utilisation Général](#-guide-dutilisation-général-le-script).

---

## 🍏 Configuration & Utilisation sous MACOS

*Note de sécurité macOS : Par défaut, Apple bloque l'exécution des scripts créés ou téléchargés sur internet. Il faut leur donner l'autorisation une seule fois avant de pouvoir double-cliquer.*

### Étape 1 : Autoriser les scripts (Une seule fois)
1. Ouvrez l'application **Terminal** sur votre Mac (via Spotlight : `Cmd + Espace` -> tapez *Terminal*).
2. Tapez `chmod +x ` (avec un espace après le x, ne validez pas tout de suite).
3. Glissez-déposez le fichier `installer_mac.command` depuis le Finder directement dans votre fenêtre de Terminal (cela va écrire son chemin automatiquement), puis appuyez sur **Entrée**.
4. Répétez la même chose pour l'autre fichier : tapez `chmod +x ` puis glissez-déposez le fichier `lancer_mac.command` et appuyez sur **Entrée**.
5. Vous pouvez fermer le Terminal définitivement.

### Étape 2 : Première installation (Une seule fois)
1. Dans le Finder, double-cliquez sur **`installer_mac.command`**.
2. Une fenêtre de Terminal s'ouvre et configure l'environnement virtuel. Attendez le message de succès, puis fermez la fenêtre.

### Étape 3 : Lancement quotidien
* Double-cliquez simplement sur **`lancer_mac.command`** pour démarrer l'aspirateur.

---

## 🔄 Guide d'Utilisation Général (Le Script)

Peu importe que vous soyez sur Windows ou Mac, une fois le programme lancé :

1. **Authentification :** Une fenêtre Google Chrome automatisée s'ouvre. Connectez-vous à votre compte *Cahier de Prépa*. Une fois sur la page d'accueil de la classe, revenez sur la console et appuyez sur **ENTRÉE**.
2. **Sélection :** Sur Chrome, naviguez dans le dossier que vous voulez aspirer (ex: *Mathématiques > DM*). Revenez sur la console et appuyez sur **ENTRÉE**.
3. **Sauvegarde :** Une fenêtre de votre système (Explorer sous Windows, Finder sous Mac) s'ouvre en arrière-plan ou au premier plan. Sélectionnez le dossier de votre ordinateur où enregistrer les documents.
4. **Boucle :** Le script télécharge tout. Vous pouvez recommencer pour un autre dossier, ou taper **`FIN`** dans la console pour fermer proprement Chrome et quitter.

---

## 🔍 Dépannage & FAQ

#### ❓ VS Code m'affiche une alerte concernant un caractère "U+fe0f"
C'est un avertissement purement visuel de l'éditeur de code lié à l'affichage des émojis (`1️⃣`, `2️⃣`, etc.). **Cela n'impacte en rien le fonctionnement du script**. Les fichiers `.bat` et `.command` exécutent le script en dehors de VS Code, donc l'alerte n'existe pas à l'exécution.

#### ❓ Sur Mac, j'ai une erreur "Permission Denied" au double-clic
Vous avez sauté l'Étape 1 de la section macOS. Vous devez donner les droits d'exécution aux fichiers `.command` en ouvrant un Terminal et en tapant `chmod +x ` suivi du chemin du fichier.

#### ❓ La fenêtre de sélection de dossier n'apparaît pas
Sous Mac ou Windows, la boîte de dialogue s'ouvre parfois derrière les autres fenêtres actives. Réduisez vos fenêtres ou vérifiez votre barre des tâches / Dock pour la faire passer au premier plan.

---

## ⚖️ Avertissement Légal
Ce script est un outil d'automatisation personnelle destiné à faciliter la révision des étudiants. Il doit être utilisé dans le respect des conditions générales d'utilisation de la plateforme *Cahier de Prépa* et ne doit pas être utilisé pour saturer les serveurs de requêtes abusives.