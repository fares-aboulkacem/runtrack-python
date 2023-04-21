def distance_to_toilet(marches, hauteur):
    hauteur_m = hauteur / 100  # conversion en mètres
    distance = marches * hauteur_m * 2 * 5 * 7  # distance parcourue en mètres
    print("Pour {marches} marches de {hauteur} cm, le gardien parcours {distance:.2f} m par semaine.")
