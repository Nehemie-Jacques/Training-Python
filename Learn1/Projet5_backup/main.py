import os
import tarfile
import jsonimport time

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Charger la config
with open("backup_config.json") as f:
    config = json.load(f)

FOLDERS = config["folders"]
BACKUP_DIR = config["backup_dir"]
RETENTION = config["retention"]

# Création du dossier backup si il n'existe pas
os.makedirs(BACKUP_DIR, exist_ok=True)

def make_backup():
    timestamp = time.strftime("%Y%m%d%H%M%S")
    archive_name = os.path.join(BACKUP_DIR, f"backup_{timestamp}.tar.gz")

    with tarfile.open(archive_name, "w:gz") as tar:
        for folder in FOLDERS:
            tar.add(folder, arcname=os.path.basename(folder))

    print(f"sauvegarde crééee: {archive_name}")
    enforce_retention()

def enforce_retention():
    backups = sorted(
        [os.path.join(BACKUP_DIR, f) for f in os.listdir(BACKUP_DIR)],
        key=os.path.getmtime,
    )
    while len(backups) > RETENTION:
        os.remove(backups[0])
        os.remove(old)
        print(f"Ancienne sauvegarde supprimée: {old}")

if __name__ == "__main__":
    make_backup()