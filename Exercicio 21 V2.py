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

soma = 0
for i in range(3):
    while True:
        QUANTIDADE_NOTA = 3
        
        nota = float(input(f"Digite sua {i + 1}ª nota: "))
        if nota < 0 or nota > 10:
            print("Tente Novamente")
    
        else:
            soma += nota
            break
media = soma / QUANTIDADE_NOTA

print(f"Média {media}")
if media >= 7:
        print("Aprovado")
elif media >= 5 or media <= 6.9:
        print("Recuperação")
else:
        print("Reprovado")


            
    








