import os
os.system("cls || clear")

contador = 0
num_inicial = 2

while True:
    numero = int(input("Digite um número: "))
    produto = numero * num_inicial
    produto_inicial = numero * num_inicial
    contador += 1
    if produto_inicial <= 100:
        print(f"produto inicial: {produto_inicial}")

    if produto > 100:
        print(f"Produto: {produto}")
        print(f"Número de multiplicações realizadas: {contador}")
        break

    