L = [8, 24, 27, 48, 2, 16, 9, 7, 84, 91]

# Initialisation de la variable "somme"
somme = 0

# Parcours de tous les éléments de la liste
for element in L:
    # Vérification si l'élément est pair
    if element % 2 == 0:
        # Ajout de l'élément à la somme
        somme += element

# Affichage du résultat
print("La somme des valeurs paires dans la liste est :", somme)
