for Nombrepremier in range(2,1001):
    if all(Nombrepremier%i!=0 for i in range(2,Nombrepremier)):
        print(Nombrepremier)