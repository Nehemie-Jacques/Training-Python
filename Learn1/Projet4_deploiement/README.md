# Automatisation DevOps – Déploiement simplifié
On va créer un script d’automatisation de déploiement qui fait trois choses simples mais puissantes :

1. Construire un projet (ex. : générer un package ou préparer des fichiers).

2. Compresser le projet (ZIP ou tar.gz).

3. Déployer automatiquement vers une machine distante via SSH/SCP.

---

# Arborescence

```bash

Projet4_deploiement/
├── main.py                # Script principal
├── deploy_config.json     # Fichier de configuration
└── mon_app/               # Notre "application" fictive
    ├── app.py
    └── utils.py

```