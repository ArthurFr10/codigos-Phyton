"""
Escreva um algoritmo que solicite duas notas para um aluno.
Caso seja menor que 0 ou maior que 10, mostre a pergunta novamente.
Calcule e mostre a média aritmética do aluno
"""


import os
os.system("cls || clear")

nota2= 0

nota1 = 0


while True:
    nota1 = float(input("Digite sua primeira nota: "))
    nota2 = float(input("Digite sua segunda nota: "))

    if (nota1 < 0 or  nota1 > 10) or (nota2 < 0 or nota2) > 10:
        print("\nA nota deve ser maior ou igual a zero ou menor ou igual a 10")
    else:
        break
        
   

nota_final = nota1 + nota2
media = nota_final / 2

print(f"Média do aluno {media}")

