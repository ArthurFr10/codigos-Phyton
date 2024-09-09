import os
os.system("cls || clear")



preco = float(input("Digite o preço de um produto: "))

def inflacao(num1):
    if num1 < 100:
         num1 = num1 * 1.1
    
    elif num1 >= 100:
         num1 = num1 * 1.2
    return num1

resultado = inflacao(preco)
print(f"{resultado} R$")  