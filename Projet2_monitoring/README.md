# Moniteur de ressources système

## Obejctif 
 Créer un script Python qui surveille en temps réel l’utilisation CPU, mémoire et disque d’une machine, et qui :

- Affiche les stats en console avec un rafraîchissement régulier

- Sauvegarde les données dans un fichier log (pour analyse ultérieure)

- Déclenche une alerte si une limite est dépassée (par ex. CPU > 80%)

- Envoie une notification si une limite est dépassée (par ex. CPU > 80%)

## Utilité du projet 

* DevOps → c’est un outil de monitoring basique que tu pourrais améliorer et intégrer dans des pipelines ou scripts d’admin.

* Cloud → le même script peut être utilisé pour surveiller un serveur cloud.

* Automatisation → alerte automatique si un seuil critique est atteint.

## Techniques Python couvertes

* Bibliothèque psutil pour récupérer les infos CPU/mémoire/disque

* Bibliothèque subprocess pour envoyer la notification

* Gestion du temps avec time

* Lecture/écriture de fichiers

* Boucles infinies avec arrêt contrôlé

* Conditions et logique métier

* Formatage lisible des données en console

## Stucture du projet :

``` bash

Projet2_monitoring/
├── main.py         # Script principal
├── README.md       # Explication du projet
└── logs/           # Dossier où seront stockés les historiques

```

## Installation 

``` bash 

pip install psutil
sudo apt install libnotify-bin


```

## Utilisation

``` bash

python3 main.py

```
