# Automatisation de tâches système

* Objectif : Créer un script qui parcourt un dossier, détecte les fichiers volumineux et les compresse. 
* Compétences : os, shutil, zipfile, manipulation fichiers/dossiers.
* Évolution possible : Ajouter un envoi automatique des fichiers compressés vers un serveur S3 (AWS).

## Travail : 

1. Parcourt d'un dossier donné

2. Repère les fichiers volumineux (taille > seuil défini)

3. Les compresse dans une archive .zip

4. (Optionnel) Envoie cette archive vers un bucket S3 (AWS)

###  Définir les paramètres du projet 

1. os → naviguer dans les fichiers et dossiers

2. zipfile → créer une archive .zip

3. boto3 (optionnel pour AWS S3)

4. pathlib (optionnel mais rend le code plus lisible)

#### Création des fichiers

# Fichier de 1 Mo
`` dd if=/dev/zero of=dossier_a_scanner/petit.txt bs=1M count=1 

# Fichier de 5 Mo
`` dd if=/dev/zero of=dossier_a_scanner/moyen.txt bs=1M count=5

# Fichier de 8 Mo
`` dd if=/dev/zero of=dossier_a_scanner/gros.txt bs=1M count=8


## Explications : 
1. dd → commande pour générer des fichiers

2. if=/dev/zero → remplit avec des octets 0

3. of= → nom du fichier

4. bs=1M → taille du bloc (1 Mo)

5. count= → nombre de blocs

# Exécution 

`` python main.py