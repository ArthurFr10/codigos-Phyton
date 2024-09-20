import os
os.system("cls || clear")

QUANTIDADE_NUMERO = 5
lista_numero = []


for i in range(QUANTIDADE_NUMERO):
    numero = int(input(f"Digite o {i + 1}ª número: "))
    lista_numero.append(numero)

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

print(f"Quantidade de números postivos: {contador_positivo}")
print(f"Quantidade de números negativos: {contador_negativo}")
print(f"Quantidade de números pares: {contador_par}")
print(f"Quantidade de números ímpares: {contador_impar}")






