import os
os.system("cls || clear")


lista_notas = []

for i in range(3):
    nota = int(input("Digite sua nota: "))
    lista_notas.append(nota)

for nota in lista_notas:
    print(f"Notas: {nota}")