"Solicite que o usuário insira em uma lista cinco nomes e mostre na ordem alfabética"

import os
os.system("cls || clear")


lista_nomes = []

for i in range(5):
    nome = input("Digite um nome: ")
    lista_nomes.append(nome)
    
lista_nomes_ordem = sorted(lista_nomes)
print(lista_nomes_ordem)    
