import os
os.system("cls || clear")
"""
Crie funções que recebam 2 números e retorne a soma, subtração, divisão e multiplicação destes dois números informados.
"""


def operacao():
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))
    opcao = int(input("Digite a operação: "))
    match(opcao):
        case 1:
            resultado = num1 - num2
            print(resultado)
        case 2:
            resultado = num1 + num2
            print(resultado)
        case 3:
            resultado = num1 * num2
            print(resultado)
        case 4:
            resultado = num1 / num2
            print(resultado)
        case _:
            print("Opção inválida")
operacao()


