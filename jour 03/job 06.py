Chaine = "abcdefghijklmnopqrstwxyz" *10
i=1

while i <= len(Chaine):
    print(Chaine[:i])

    Chaine=Chaine[i:]

    i+=1