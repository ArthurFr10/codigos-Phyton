"""
Escreva um programa que solicite ao usuário o ano de nascimento e, utilizando uma função, retorne com a idade do usuário.
"""

import os
os.system("cls || clear")


data_nascimento = int(input("Digite seu ano de nascimento: "))

def calculo(data):
    idade = 2024 - data
    return idade

idade = calculo(data_nascimento)
print(f"Idade: {idade}")