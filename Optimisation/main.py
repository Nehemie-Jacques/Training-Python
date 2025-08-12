# 1. Reformulation du problème
# Nous avons : 

# Produits :
# Bougies B : coût 5, prix 12, volume 200 cm³, demande max 150
# Savons S : coût 3, prix 8, volume 100 cm³, demande max 200
# Bijoux J : coût 10, prix 25, volume 50 cm³, demande max 100

# Contraintes :
# Budget total ≤ 1500 (en milliers de FCFA)
# Stockage total ≤ 20 000 cm³
# Ne pas dépasser les demandes max.

# Objectif : maximiser le profit total : Profit_unité = Prix_vente - Coût_fabrication


# 2. Calcul préalable des profits unitaires

# Bougie : 12 − 5 = 7
# Savon : 8 − 3 = 5
# Bijou : 25 − 10 = 15

# 3. Approche de résolution du problème 

# On va tester toutes les combinaisons possibles de produits et de quantités pour trouver la meilleure combinaison de produits et de quantités qui maximise le profit total.
# Tou en respectant les contraintes du probleme. (Budget total ≤ 1500 (en milliers de FCFA), Stockage total ≤ 20 000 cm², Ne pas dépasser les demandes max.)

# 4. Algorithme de resolution

# Création de dictionnaires "{...}" pour stocker les côts, prix, volumes et demandes max pour chaque produit.
cout = {"B": 5, "S": 3, "J": 10}
prix = {"B": 12, "S": 8, "J": 25}
volume = {"B": 200, "S": 100, "J": 50}
max_demande = {"B": 150, "S": 200, "J": 100}

BUDGET_MAX = 1500
VOLUME_MAX = 20000

profit_unit = {}  # Dictionnaire pour stocker les profits unitaires

for produit in cout:
    prix_vente = prix[produit] # Recupere le prix de vente du produit
    cout_fabrication = cout[produit] # Recupere le cout de fabrication du produit
    profit = prix_vente - cout_fabrication # Calcule le profit unitaire
    profit_unit[produit] = profit # Stocke le profit unitaire dans le dictionnaire

max_profit = 0 # Variable pour stocker le profit maximum, initialisee a 0
best_combination = None # Variable pour stocker la meilleure combinaison, initialisee a None

for b in range(max_demande["B"] + 1):      # parcourte toutes les quantites de bougies possibles pour b de 0 à 150
    for s in range(max_demande["S"] + 1):      # parcourte toutes les quantites de savons possibles pour s de 0 à 200
        for j in range(max_demande["J"] + 1):      # parcourte toutes les quantites de bijoux possibles pour j de 0 à 100
            budget = b * cout["B"] + s * cout["S"] + j * cout["J"]     # calcule le coût total de production pour la combinaison (b, s, j)
            vol = b * volume["B"] + s * volume["S"] + j * volume["J"]     # calcule le volume total de production pour la combinaison (b, s, j)

            if budget <= BUDGET_MAX and vol <= VOLUME_MAX: 
            # Cette condition filtre les combinaisons : on ne conserve que celles dont le budget total est inférieur ou égal à BUDGET_MAX et dont le volume total est inférieur ou égal à VOLUME_MAX. Si l’une des deux contraintes est violée, on ignore la combinaison (on ne calcule pas son profit).
                profit = b * profit_unit["B"] + s * profit_unit["S"] + j * profit_unit["J"]     # calcule le profit total pour la combinaison (b, s, j) si les contraintes sont respectées

                if profit > max_profit: 
                # Cette condition met a jour le profit maximum et la meilleure combinaison si le profit calcule est supérieur au profit maximum actuel.
                    max_profit = profit   # met a jour le profit maximum
                    best_combination = (b, s, j)   # met a jour la meilleure combinaison

print("La meilleure combinaison pour maximiser le profit est : ", best_combination)
print("Le profit maximum est de : ", max_profit, "milliers FCFA")
