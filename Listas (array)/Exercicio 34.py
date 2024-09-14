

import os
os.system("cls || clear")

QUANTIDADE_NOTA = 3
soma = 0
lista_vetor = []

for i in range(QUANTIDADE_NOTA):
    nota = float(input(f"Digite a sua {i+1}ª nota: "))
    lista_vetor.append(nota)

soma = sum(lista_vetor)
media = soma / QUANTIDADE_NOTA

for contador, nota in enumerate (lista_vetor):
    print(f"{contador + 1}ª nota: {nota}")
print(f"Média: {media}")
