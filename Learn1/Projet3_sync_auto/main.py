from watchdog.observers import Observer     # lance un thread qui écoute le système de fichiers.
from watchdog.events import FileSystemEventHandler      # classe de base à étendre pour réagir aux événements (create/modify/delete).
import time
import os
import shutil
from datetime import datetime

DOSSIER_SOURCE = "dossier_source"
DOSSIER_BACKUP = "dossier_backup"

class MonHandler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory:
            self.copier_fichier(event.src_path)

    def on_modified(self, event):
        if not event.is_directory:
            self.copier_fichier(event.src_path)

    def on_deleted(self, event):
        if not event.is_directory:
            self.supprimer_fichier(event.src_path)

    def copier_fichier(self, chemin_source):
        nom_fichier = os.path.basename(chemin_source)
        chemin_backup = os.path.join(DOSSIER_BACKUP, nom_fichier)
        shutil.copy2(chemin_source, chemin_backup)
        print(f"[{self.timestamp()}] Fichier synchronisé : {nom_fichier}")

    def supprimer_fichier(self, chemin_source):
        nom_fichier = os.path.basename(chemin_source)
        chemin_backup = os.path.join(DOSSIER_BACKUP, nom_fichier)
        if os.path.exist(chemin_backup):
            os.remove(chemin_backup)
            print(f"[{self.timestamp()}] Fichier supprimé : {nom_fichier}")
        else:
            print(f"[{self.timestamp()}] Fichier non trouvé : {nom_fichier}")

    def timestamp(self):
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

if __name__ == "__main__":
    # Création des dossiers de source et de backup si ils n'existent pas
    os.makedirs(DOSSIER_SOURCE, exist_ok=True)
    os.makedirs(DOSSIER_BACKUP, exist_ok=True)

    event_handler = MonHandler()
    observer = Observer()
    observer.schedule(event_handler, DOSSIER_SOURCE, recursive=True)

    observer.start()
    print(f"👀 Surveillance en cours sur '{DOSSIER_SOURCE}'...")
    print(f"📂 Sauvegarde vers '{DOSSIER_BACKUP}'...")

    try:
        while True:
            time.sleep(1)
    except keyboardInterrupt:
        observer.stop()

    observer.join()