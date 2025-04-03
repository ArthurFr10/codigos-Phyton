import os
os.system("cls || clear")

lista_numeros = [1,2,3,4,5,6]

#realizando cópia da lista original
lista_organizada = sorted(lista_numeros, reverse=True)

print(f"Lista original: {lista_numeros}")

print(f"Lista modificada: {lista_organizada}")