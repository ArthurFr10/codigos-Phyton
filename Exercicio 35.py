import os
os.system("cls || clear")

QUANTIDADE_NOTA = 4
lista_notas = []

for i in range(QUANTIDADE_NOTA):
    nota = float(input(f"Digite a sua {i + 1}ª nota: "))
    lista_notas.append(nota)

soma = sum(lista_notas)
media = soma / QUANTIDADE_NOTA


if media >= 7:
    situacao = "Aprovado"

elif media >= 5 and media < 7:
    situacao = "Recuperacao"

else:
    situacao = "Reprovado"


print(f"Resultado Final: {situacao}")