L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]  # la liste donnée

minimum = L[0]  # initialisation de la variable minimum à la première valeur de la liste
maximum = L[0]  # initialisation de la variable maximum à la première valeur de la liste

for wof in L:  # parcours de tous les éléments de la liste
    if wof < minimum:  # si l'élément actuel est inférieur au minimum actuel
        minimum = wof  # mettre à jour la variable minimum
    if wof > maximum:  # si l'élément actuel est supérieur au maximum actuel
        maximum = wof  # mettre à jour la variable maximum

print("Le minimum de la liste est :", minimum)  # affichage du résultat minimum
print("Le maximum de la liste est :", maximum)  # affichage du résultat maximum
