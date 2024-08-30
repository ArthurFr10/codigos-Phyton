"""
Escreva um algoritmo que leia três notas de um aluno.

Caso seja menor que 0 ou maior que 10, mostre a pergunta novamente.

Após receber as notas dentro dos parâmetros acima, calcule a média e verifique se o aluno está
aprovado, recuperação ou reprovado considerando os seguintes critérios:
Se a média for a partir de 7, aprovado
Se a média for entre 5 e 6,9, o aluno está de recuperação
Caso seja menor que 5 o aluno está reprovado
"""
import os
os.system("cls || clear ")

contador = 0
soma = 0

while True:
    primeira_nota = int(input("Digite a primeira nota: "))
    segunda_nota = int(input("Digite a segunda nota: "))
    terceira_nota = int(input("Digite a terceira nota: "))
    soma = primeira_nota + segunda_nota + terceira_nota
    media = soma / 3

    if (primeira_nota < 0 or primeira_nota > 10) or (segunda_nota < 0 or segunda_nota> 10) or (terceira_nota < 0 or terceira_nota > 10):
        print("Tente novamente")
    elif media >= 7:
        print("Está aprovado")
        break
    elif media >= 5 or media <= 6.9:
        print("Voce está de recuperação")
        break
    else:
        print("Voce está reprovado")
        break

