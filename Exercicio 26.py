import os
os.system("cls || clear")

numero = int(input("Digite um número: "))


def par_impar (num1):
    if num1 % 2 == 0:
        print("Par")
    else:
        print("ímpar")

par_impar(numero)
    