import os
os.system("cls || clear")



primeira_nota = int(input("Digite sua primeira nota: "))
segunda_nota = int(input("Digite sua segunda nota: "))

QUANTIDADE_NOTAS = 2

def calcular_media (num1, num2):
    media2 = (num1 + num2) / QUANTIDADE_NOTAS
    if media2 >= 7 and media2 <= 10:
        print("Aprovado")
    else:
        print("Tente Novamente")

def calcular_media2 (num1, num2):
    media4 = (num1 + num2) / QUANTIDADE_NOTAS
    if media4 < 7 and media4 >= 0:
        print("Reprovado")


calcular_media(primeira_nota, segunda_nota)
calcular_media2(primeira_nota, segunda_nota)

    