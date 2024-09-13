"""
Crie um algoritmo que aceite apenas 6 valortes inteiros, positivos e pares
Em seguida, mostre na tela os valortes lidos na ordem inversa.
Caso seja informado um número diferente dos critérios apresentados acima, repita a pergunta para o usuário.
"""

import os
os.system("cls || clear")
QUANTIDADE_NUMERO = 3
lista_numero = []

## FAZER CODIGO EM CASA
for i in range(QUANTIDADE_NUMERO):
    numero = int(input(f"Digite o {i+1}ª número: "))
    lista_numero.append(numero)

def calculo(a):
    positivo = a
    par = a
    par >= 0
    positivo % 2 == 0
    return par, positivo

lista = calculo(lista_numero)
for numero in lista_numero:
    print(lista_numero)
