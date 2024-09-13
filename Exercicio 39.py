import os
os.system("cls || clear")

QUANTIDADE_NUMERO = 10
lista_numero = []


for i in range(QUANTIDADE_NUMERO):
    numero = int(input(f"Digite o seu {i+1}ª número: "))
    lista_numero.append(numero)

def calculo(lista_numero):
    lista_atualizada = []
    for numero in lista_numero:
        if numero < 0:
            numero = 0

        lista_atualizada.append(numero)
    return lista_atualizada
lista_numero = calculo(lista_numero)
for numero in lista_numero:
    print(numero)
    






