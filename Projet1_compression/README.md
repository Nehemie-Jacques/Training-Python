# Automatisation de tâches système

## 📌 Objectif
Créer un script Python qui parcourt un dossier, détecte les fichiers volumineux et les compresse dans une archive .zip.
En option, le script peut envoyer cette archive vers un bucket AWS S3.

---

## 🛠 Compétences mobilisées
- os → navigation dans les fichiers et dossiers.

- zipfile → création d’archives .zip.

- shutil → manipulation de fichiers et dossiers.

- pathlib (optionnel) → rendre le code plus lisible.

- boto3 (optionnel) → interaction avec AWS S3.

---

## Arborescence 
``` bash

Projet1_compression/
├── main.py         # Script principal
├── README.md       # Explication du projet
└── dossier_a_scanner/           # Dossier à scanner

``` 

--- 

## 🔄 Fonctionnement
Parcourt d'un dossier donné.

- Détection des fichiers volumineux (taille > seuil défini).

- Compression dans une archive .zip.

- (Optionnel) Envoi de l’archive vers un bucket AWS S3.

---

## ⚙️ Paramètres du projet
* Seuil de taille : ajustable dans le code (ex. 5 Mo).

* Chemin du dossier : modifiable dans le script.

---

## 📂 Création de fichiers de test
Exécuter les commandes suivantes dans un terminal Linux/macOS pour créer des fichiers de tailles différentes dans dossier_a_scanner :

``` bash

# Fichier de 1 Mo
dd if=/dev/zero of=dossier_a_scanner/petit.txt bs=1M count=1

# Fichier de 5 Mo
dd if=/dev/zero of=dossier_a_scanner/moyen.txt bs=1M count=5

# Fichier de 8 Mo
dd if=/dev/zero of=dossier_a_scanner/gros.txt bs=1M count=8

```

---

### Explication des paramètres :

* dd → commande pour générer des fichiers.

* if=/dev/zero → remplit le fichier avec des octets nuls.

* of= → nom et emplacement du fichier créé.

* bs=1M → taille du bloc (1 Mo).

* count= → nombre de blocs.

---

## ▶️ Exécution
Lancer le script avec :

``` bash
python main.py

(Si boto3 est utilisé pour AWS, configurez vos identifiants AWS via aws configure.)

