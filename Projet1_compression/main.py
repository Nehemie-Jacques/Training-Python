import os 

DOSSIER_CIBLE = "dossier_a_scanner"
TAILLE_MIN = 5 * 1024 * 1024  # 5 Mo en octets

def trouver_fichiers_volumineux(dossier):
    fichiers_trouves = []

    for racine, _, fichiers in os.walk(dossier):   # parcours le dossier et ses sous-dossiers
    # os.walk renvoie un tuple (racine, sous-dossiers, fichiers)  explore le dossier et ses sous-dossiers
        for fichier in fichiers:
            chemin_complet = os.path.join(racine, fichier)   
            taille = os.path.getsize(chemin_complet)  # obtenir la taille du fichier en octets

            if taille >= TAILLE_MIN:
                fichiers_trouves.append((chemin_complet, taille))
    
    return fichiers_trouves  # renvoie une liste de tuples (chemin, taille)

if __name__ == "__main__":
    resultats = trouver_fichiers_volumineux(DOSSIER_CIBLE)

    if resultats :
        print("Fichiers volumineux trouves :")
        for chemin, taille in resultats:
            print(f"- {chemin} ({taille / (1024 * 1024):.2f} Mo)")
    else:
        print("Aucun fichier volumineux trouv�.")