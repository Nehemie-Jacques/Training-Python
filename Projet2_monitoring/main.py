import psutil  #  permet de récupérer l’état des ressources système (CPU, RAM, disque, réseau…).
import time  #  permet de mettre en pause le programme pour une certaine durée.
from datetime import datetime  # permet de travailler avec des dates et heures actuelles.
import os  # permet de manipuler les chemins, les fichiers et les directories
import subprocess  # permet d’exécuter des commandes système (ici notify-send pour envoyer une notification).

CPU_LIMIT = 80  # % d'utilisation CPU déclenchant une alerte
MEM_LIMIT = 80  # % d'utilisation RAM déclenchant une alerte
LOG_DIR = "logs"
LOG_FILE = "os.path.join(LOG_DIR, 'monitoring.log')"    # Chemin vers le fichier de log

os.makedirs(LOG_DIR, exist_ok=True)    # Création du dossier de logs si il n'existe pas

def send_notification(title, message):
# On définit send_notification qui utilise la commande notify-send via subprocess.run.
    subprocess.run(["notify-send", title, message])

print("Monitoring started...")

try: 
    while True:
        # Récupération des données sur le système
        cpu = psutil.cpu_percent(interval=1)  # mesure le CPU sur 1 seconde.
        memory = psutil.virtual_memory().percent  #  récupère le pourcentage de RAM utilisée.
        disk = psutil.disk_usage('/').percent  #  récupère le pourcentage de disque utilisé.

        # création d'un timestamp(date et heure)
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Affichage des données en console
        print(f"[{now}] CPU: {cpu}% | RAM: {memory}% | DISK: {disk}%")

        # Écriture dans le fichier log
        with open(LOG_FILE, "a") as f:
        # Mode "a": ajoute les nouvelles lignes sans effacer les précédentes.
            f.write(f"{now} - CPU: {cpu}% | RAM: {memory}% | DISK: {disk}%\n")

        if cpu > CPU_LIMIT:
            alert_msg = f"CPU au-dessus de la limite : {cpu}%"
            print("Alerte : CPU au-dessus de la limite !")
            send_notification("Alerte CPU", alert_msg)

        if memory > MEM_LIMIT:
            alert_msg = f"Mémoire au-dessus de la limite : {memory}%"
            print("Alerte : Mémoire au-dessus de la limite !")
            send_notification("Alerte Mémoire", alert_msg)
        
        time.sleep(3)  # Attente de 3 secondes avant la prochaine itération
        

except KeyboardInterrupt:  # Permet de sortir proprement de la boucle si on fait Ctrl+C.
    print("Monitoring stoppé par l'utilisateur.")