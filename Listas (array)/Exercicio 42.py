import os
os.system("cls || clear")

"""
Altere o algoritmo que acabou de criar e faça com que o usuário insira números inteiros até que seja inserido o número 0
1. A quantidade de números postivos que são pares
2. A quantidade de números ímpares
3. A quantidade de números negativos
4. A quantidade de números inseridos
"""

QUANTIDADE_NUMERO = 5
lista_numero = []
contador_total = 0

while True:
        numero = int(input(f"Digite um número: "))
        lista_numero.append(numero)
        contador_total += 1
        if numero == 0:
            break

def positivo_negativo(a):
    contador_positivo = 0
    contador_negativo = 0
    for numero in a:
        if numero >= 0:
            contador_positivo += 1
        else:
            contador_negativo += 1
    return contador_positivo, contador_negativo

contador_positivo, contador_negativo = positivo_negativo(lista_numero)

def par_impar(a):
    contador_par = 0
    contador_impar = 0
    for numero in a:
        if numero % 2 == 0:
            contador_par += 1
        else:
            contador_impar += 1
    return contador_par, contador_impar

contador_par, contador_impar = par_impar(lista_numero)

def postivo_par(a):
    par_positivo = 0
    for numero in a:
        if numero > 0 and numero % 2 == 0:
            par_positivo += 1
    return par_positivo

numeros_pares_postivos = postivo_par(lista_numero)

print(f"Quantidade de números positivos que são pares: {numeros_pares_postivos}")
print(f"Quantidade de números ímpares: {contador_impar}")
print(f"Quantidade de números negativos: {contador_negativo}")
print(f"Quantidade de números inseridos: {contador_total}")