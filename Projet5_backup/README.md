# Automatisation de sauvegardes (Backup Manager)
Objectif : Créer un script Python qui automatise les sauvegardes de fichiers/dossiers importants en les copiant dans un dossier backups/ compressé avec horodatage.

---

# Arborescence

```bash

Projet5_backup/
├── main.py             # le script Python principal
├── backup_config.json  # fichier de configuration (ce qu’on sauvegarde, où, combien)
└── backups/            # dossier qui contiendra les sauvegardes compressées


```

---

# Fonctionnement

1. Lecture config → charge la liste des dossiers à sauvegarder, où les stocker, combien garder.

2. Création archive → chaque sauvegarde est un .tar.gz nommé avec la date/heure (backup-20250818-051230.tar.gz).

3. Rétention → si le nombre de sauvegardes dépasse la limite (retention), les plus anciennes sont supprimées automatiquement.