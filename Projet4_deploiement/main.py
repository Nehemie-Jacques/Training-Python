import os
import tarfile
import paramiko
import json
from scp import SCPClient

# Charger la configuration
with open("deploy_config.json") as f:
    config = json.load(f)

SERVER = config["server"]
USER = config["user"]
PASSWORD = config["password"]
REMOTE_PATH = config["remote_path"]

# Cration d'une archive tar.gz du projet local
def make_archive(source_dir, archive_name="package.tar.gz"):
    with tarfile.open(archive_name, "w:gz") as tar:
        tar.add(source_dir, arcname = os.path.basename(source_dir))
    print(f"Archive created: {archive_name}")
    return archive_name

# Envoi de l'archive sur le serveur distant
def deploy(archive):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(SERVER, username=USER, password=PASSWORD)

    with SCPClient(ssh.get_transport()) as scp:
        scp.put(archive, REMOTE_PATH)
        print(f"Archive deployed to {SERVER}:{REMOTE_PATH}")

    # Décompression de l'archive coté serveur
    stdin, stdout, stderr = ssh.exec_command(f"cd {REMOTE_PATH} && tar -xzf {archive}")
    print(stdout.read().decode(), stderr.read().decode())
    ssh.close()


if __name__ == "__main__":
    archive = make_archive("Projet4_deploiement")
    deploy(archive)