"""
Escreva um algoritmo que pergunte ao usuário se deseja inserir mais uma nota.
Mostre um menu conforme o descrito abaixo:
S - Inserir mais uma nota
P - Ver quantas notas foram inseridas
N - Calcular a média aritmética das notas informadas.
O programa deve mostrar a média aritmética para o usuário
"""
import os
os.system("cls || clear")
contador = 1
nota2 = 0
nota = 0
nota_final = 0
nota = float(input("Digite uma nota: "))

while True:
    print("""
        -------MENU-------    
    S - Inserir mais uma nota
    P - Ver quantas notas foram inseridas
    N - Calcular a média aritmética das notas informadas.
    """)
    opcao = str(input("Digite a letra correspondente: ")).upper()
    
    match(opcao):
        case "S":
            nota2 = float(input("Insira mais uma nota: "))
            contador += 1
            nota_final += nota2
        case "P":
            print(f"Quantidade de notas inseridas: {contador}")
        case "N":
            
            media = (nota_final + nota) / contador
            float(input(f"Média aritmética: {media}"))
            break


            
        

        

