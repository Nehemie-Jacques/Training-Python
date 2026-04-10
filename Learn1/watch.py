from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import subprocess
import time
import os

class Watcher(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path.endswith(".py"):
            os.system("clear")  # nettoie la console
            print(f"🔁 Re-running {event.src_path}...\n")
            subprocess.run(["python3.13", "main.py"])


observer = Observer()
observer.schedule(Watcher(), path=".", recursive=False)
observer.start()

try:
    print("👀 Watching for changes... Ctrl+C to stop.")
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()

observer.join()
