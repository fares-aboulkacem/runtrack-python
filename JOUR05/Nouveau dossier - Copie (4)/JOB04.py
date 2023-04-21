def caesar_cipher(message, shift):
    ciphered_message = ""
    for letter in message:
        if letter.isalpha():
            # Décale la lettre de shift rangs dans l'alphabet
            # en prenant en compte le dépassement de 'z' vers 'a' et vice-versa
            shifted_letter = chr((ord(letter) - 97 + shift) % 26 + 97)
        else:
            # Conserve les caractères non alphabétiques
            shifted_letter = letter
        ciphered_message += shifted_letter
    return ciphered_message
