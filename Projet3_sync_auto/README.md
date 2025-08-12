# Gestionnaire de tâches en ligne de commande

- Objectif : Stocker des tâches avec priorité dans un fichier JSON, les lister et les marquer comme terminées.

- Compétences : lecture/écriture JSON, boucles, conditions, manipulation de listes/dictionnaires.

- Évolution possible : Ajouter la planification automatique d’alertes avec schedule ou APScheduler.

---

## Explication

On part sur un outil de synchronisation automatique de dossiers (un peu comme un mini-Nextcloud en local), qui pourrait servir :

* En DevOps pour synchroniser des logs ou configs vers un serveur distant.

* En Cloud pour backup automatique de fichiers dans un dossier local vers un bucket (exemple : AWS S3, Google Drive, etc.).

* En automatisation pour maintenir une copie à jour entre deux répertoires.

---

## Idée générale du projet

1. Surveiller un dossier avec watchdog pour détecter toute modification (ajout, suppression, modification de fichiers).

2. Synchroniser automatiquement ces fichiers avec un dossier de sauvegarde local ou un serveur distant.

3. Garder un log des fichiers synchronisés.

4. Notifier l’utilisateur quand un transfert est fait.

---

## Architecture du projet

``` bash

Projet3_sync_auto/
│── dossier_source/       # Dossier surveillé
│── dossier_backup/       # Dossier de sauvegarde
│── main.py               # Script principal
│── sync.log              # Journal des synchronisations
│── README.md

```
---

## Fonctionnalités prévues

* Détection en temps réel des changements via watchdog.

* Copie automatique des fichiers modifiés dans le dossier de backup.

* Gestion des suppressions (si un fichier est supprimé dans source, il l’est aussi dans backup).

* Logs horodatés pour suivi.

* Notification système quand une synchronisation est effectuée.

