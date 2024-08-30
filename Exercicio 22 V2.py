import os
os.system("cls || clear")

soma = 0
contador = 0

while True:
    nota = float(input("Digite uma nota: "))
    contador =+ 1
    soma =+ nota

    resposta = input("Deseja inserir mais uma nota? ").upper()

    if resposta == "N".upper():
        break
media = soma / contador
print(f"Média: {media}")