import re
import hashlib

while True:
    password = input("Veuillez entrer un mot de passe : ")

    if len(password) < 8:
        print("Le mot de passe doit contenir au moins 8 caractères.")
        continue
    elif not re.search("[a-z]", password):
        print("Le mot de passe doit contenir au moins une lettre minuscule.")
        continue
    elif not re.search("[A-Z]", password):
        print("Le mot de passe doit contenir au moins une lettre majuscule.")
        continue
    elif not re.search("[0-9]", password):
        print("Le mot de passe doit contenir au moins un chiffre.")
        continue
    elif not re.search("[!@#$%^&*]", password):
        print("Le mot de passe doit contenir au moins un caractère spécial (!, @, #, $, %, ^, &, *).")
        continue
    else:
        
        print("Mot de passe valide !")
        break

hash_object = hashlib.sha256(password.encode())
hex_dig = hash_object.hexdigest()

print("Le mot de passe crypté est :", hex_dig)
