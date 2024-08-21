import os
os.system("cls || clear")

#Solicitando dados
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

#Calculando
if (idade < 18 or idade > 65):
    print("Voce não é obrigado a votar")
else:
    print("Voce é obrigado a votar")

#Exibindo resultados

