L = [7, 11, 42, 39, 2]  # création de la liste L

print("Liste originale :", L)  # affichage de la liste originale

for index in range(len(L)):  # boucle pour parcourir tous les éléments de la liste
    L[index] += 1  # ajouter 1 à chaque élément de la liste

print("Liste modifiée :", L)  # affichage de la liste modifiée
