import os
os.system("cls || clear")

contador = 0
soma = 0
while True:
    nota = int(input("Digite sua nota: "))
    contador += 1
    soma += nota
    media = soma / contador

    if nota < 0:
        print(f"Média: {media}")
        break

    