import os
os.system("cls || clear")


soma = 0

#Solicitando dados
for i in range(4):
    nota = float(input("Digite sua nota: "))
    soma = soma + nota


#calculando

media = soma / 4




#Exibindo resultados
print(f"Média: {media}")
