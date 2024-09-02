import os
os.system("cls || clear")

contador = 0

while True:
    numero = int(input("Digite seu número: "))
    if numero < 0:
        contador += 1
    elif numero >= 0:
        break

print(f"Quantidade de números negativos: {contador}")

