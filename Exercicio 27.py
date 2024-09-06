import os
os.system("cls || clear")
contador_par = 0
contador_impar = 0

for i in range(6):
    numero = int(input(f"Digite o {i + 1}ª número: "))

def par(num1):
    total = num1 % 2 == 0 
    contador_par += 1
    return total


def impar(num1):
    total = num1 % 2 != 0
    contador_impar += 1
    return total



