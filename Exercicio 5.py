import os
os.system("cls || clear")



#Solicitando dados
primeiro_numero = int(input("Digite o primeiro número: "))
segundo_numero = int(input("Digite o segundo número: "))
opcao = input("Digite uma opção(+-*/): ")

#Calculando
match(opcao):
    case "+":
        resultado = primeiro_numero + segundo_numero
    case "-":
        resultado = primeiro_numero - segundo_numero
    case "*":
        resultado = primeiro_numero * segundo_numero
    case "/":
        resultado = primeiro_numero / segundo_numero
    case _:
        print("Opção inválida")

#Exibindo resultados
print(f"Resultado: {resultado}")