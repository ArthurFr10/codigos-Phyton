"""
Escreva um algoritmo que pergunte ao usuário se deseja inserir mais uma nota, se a resposta do usuário
 for "N", o programa fará a média aritmética das notas informadas
e mostrará a média aritmética para o usuário.

obs: Use um contador dentro do laço de repetição para contar a quantidade de iterações (loops)
"""
import os
os.system("cls || clear")

contador = 1
nota2 = 0
nota = 0
nota_final = 0
nota = float(input("Digite uma nota: "))

while True:
    print(f"Quantidade de loops: {contador}")
    opcao = str(input("Deseja inserir mais uma nota? ")).upper()
    
    match(opcao):
        case "S":
            nota2 = float(input("Insira mais uma nota: "))
            
            contador += 1
            nota_final += nota2

        case "N":
            media = (nota_final + nota) / contador
            float(input(f"Média aritmética: {media}"))
            break

        case _:
            print("Tente novamente")