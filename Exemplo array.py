import os
os.system("cls || clear")


lista_notas = []

for i in range(2):
    nota = float(input("Digite uma nota: "))
    lista_notas.append(nota)


for nota, in enumerate(lista_notas):
    print(f"{nota + 1}º nota: {nota}")