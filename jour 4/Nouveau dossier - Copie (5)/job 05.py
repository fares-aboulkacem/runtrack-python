# Création de la liste L
L = [1, 2, 3, 4, 5]

# Affichage de L[1]
print("La valeur de L[1] est :", L[1])

# Fonction pour remplacer L[3] par la somme de L[2] et L[4]
def replace_L3(L):
    L[3] = L[2] + L[4]

# Appel de la fonction pour modifier L[3]
replace_L3(L)

# Affichage de la dernière valeur de la liste
print("La dernière valeur de la liste est :", L[-1])
