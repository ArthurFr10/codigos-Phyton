import os
os.system("cls || clear")

soma = 0
quantidade_nota = 3
#Solicitando dados



for i in range(3):
    nota = float(input("Digite sua nota: "))
    soma = soma + nota




#calculando
media = soma / quantidade_nota

if media >= 7:
    print("Aprovado")
elif media < 4:
    print("reprovado")
else:
    print("recuperação")



#Exibindo resultados


