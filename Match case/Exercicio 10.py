import os
os.system("cls || clear")

peso_masculino = 0
peso_feminino = 0

#Solicitando dados
altura = float(input("Digite sua altura: "))
sexo = str(input("Digite o caractere correspondente ao seu sexo: "))

#Calculando
match(sexo):
    case "M" | "m":
        peso_masculino = (72.7 * altura) - 58
        print(f"Peso ideal: {peso_masculino:.2f} Kg")
    case "F" | "f":
        peso_feminino = (62.1 * altura) - 44.7
        print(f"Peso ideal: {peso_feminino:.2f} Kg")
    case _:
        print("Opção Inváida")        


#Exibindo resultados

