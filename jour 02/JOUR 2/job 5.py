num1 = 10
num2 = 20
operator = '+' 
def calcul(num1, operator, num2):
    if operator == '+' :
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2     
    else:
        print("operator invalide")
print(calcul(10,'-',20))
print(calcul(10,'+',20))
print(calcul(10,'*',20))