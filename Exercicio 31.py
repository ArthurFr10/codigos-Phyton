import os
os.system("cls || clear")
soma = 0
QUANTIDADE_NOTA = 3
for i in range(QUANTIDADE_NOTA):
    nota = float(input(f"Digite a {i + 1}ª nota: "))
    soma += nota
    def calcular_media():
        media = soma / QUANTIDADE_NOTA
        print(media)
        return media
media = calcular_media()
