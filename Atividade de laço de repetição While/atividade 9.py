import os
os.system("cls || clear")

contador = 0
soma = 0
VALOR_MAXIMO = 200

while True:
    numero = int(input("Digite um número: "))
    if numero % 2 != 0:
        soma += numero
        contador += 1

    if soma > VALOR_MAXIMO:
        break

print(f"Total de números ímpares: {contador}")
print(f"Soma: {soma}")