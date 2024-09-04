import os
os.system("cls || clear")

quantidade_nota = 2
def calcular_media(primeira_nota, segunda_nota):
    soma = primeira_nota + segunda_nota
    resultado = soma / quantidade_nota
    return resultado

primeira_nota = int(input("Digite sua primeira nota: "))
segunda_nota = int(input("Digite sua segunda nota: "))

media = calcular_media(primeira_nota, segunda_nota)

print(f"Média: {media}")
