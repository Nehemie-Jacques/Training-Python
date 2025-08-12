from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler  
import time
import os

DOSSIER_SOURCE = "dossier_source"

class MonHandler(FileSystemEventHandler):
    def on_created(self, event):
        print(f"Nouveau fichier créé : {event.src_path}")

    def on_modified(self, event):
        print(f"Fichier modifié : {event.src_path}")

    def on_deleted(self, event):
        print(f"Fichier supprimé : {event.src_path}")

if __name__ == "__main__":
    if not os.path.exists(DOSSIER_SOURCE):
        os.makedirs(DOSSIER_SOURCE)

    event_handler = MonHandler()
    observer = Observer()
    observer.schedule(event_handler, DOSSIER_SOURCE, recursive=True)

    observer.start()
    print(f"👀 Surveillance en cours sur '{DOSSIER_SOURCE}'...")

    try:
        while True:
            time.sleep(1)
    except keyboardInterrupt:
        observer.stop()

    observer.join()