import os
os.system("cls || clear")

def ler_numero_valido():
    """Lê um número inteiro, positivo e par do usuário.
    Continua solicitando até que o usuário digite um valor válido."""

    while True:
    
            numero = int(input("Digite um número inteiro, positivo e par: "))
            if numero > 0 and numero % 2 == 0:
                return numero
            else:
                print("Número inválido! Digite um número inteiro, positivo e par.")

def ler_seis_numeros():
    """Lê seis números inteiros, positivos e pares do usuário e retorna uma lista."""

    numeros = []
    for _ in range(6):
        numero = ler_numero_valido()
        numeros.append(numero)
    return numeros

def imprimir_numeros_inversos(numeros):
    """Imprime os números de uma lista na ordem inversa."""

    print("Números na ordem inversa:")
    for numero in reversed(numeros):
        print(numero)

# Programa principal
numeros = ler_seis_numeros()
imprimir_numeros_inversos(numeros)