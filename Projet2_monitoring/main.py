import psutil
import time
from datetime import datetime
import os
import subprocess

CPU_LIMIT = 80  # % d'utilisation CPU déclenchant une alerte
MEM_LIMIT = 80  # % d'utilisation RAM déclenchant une alerte
LOG_DIR = "logs"
LOG_FILE = "os.path.join(LOG_DIR, 'monitoring.log')"    # Chemin vers le fichier de log

os.makedirs(LOG_DIR, exist_ok=True)    # Création du dossier de logs si il n'existe pas

print("Monitoring started...")

try: 
    while True:
        # Récupération des données sur le système
        cpu = psutil.cpu_percent(interval=1)
        memory = psutil.virtual_memory().percent
        disk = psutil.disk_usage('/').percent

        # création d'un timestamp(date et heure)
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Affichage des données en console
        print(f"[{now}] CPU: {cpu}% | RAM: {memory}% | DISK: {disk}%")

        # Écriture dans le fichier log
        with open(LOG_FILE, "a") as f:
            f.write(f"{now} - CPU: {cpu}% | RAM: {memory}% | DISK: {disk}%\n")

        if cpu > CPU_LIMIT:
            alert_msg = f"CPU au-dessus de la limite : {cpu}%"
            print("Alerte : CPU au-dessus de la limite !")
            send_notification("Alerte CPU", alert_msg)

        if memory > MEM_LIMIT:
            alert_msg = f"Mémoire au-dessus de la limite : {memory}%"
            print("Alerte : Mémoire au-dessus de la limite !")
            send_notification("Alerte Mémoire", alert_msg)
        
        time.sleep(5)  # Attente de 5 secondes avant la prochaine itération
        

except KeyboardInterrupt:
    print("Monitoring stoppé par l'utilisateur.")