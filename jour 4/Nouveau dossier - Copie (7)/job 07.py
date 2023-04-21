L = [8, 24, 48, 2, 16]

# Initialisation du compteur de multiples de 3
compteur = 0

# Parcourir chaque élément de la liste
for element in L:
    # Vérifier si l'élément est un multiple de 3
    if element % 3 == 0:
        # Si c'est le cas, ajouter 1 au compteur
        compteur += 1

# Afficher le résultat
print("Le nombre de multiples de 3 dans la liste est :", compteur)
