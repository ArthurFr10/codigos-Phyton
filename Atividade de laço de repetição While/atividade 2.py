import os
os.system ("cls || clear")


while True:

    numero = int(input("Digite um número: "))
    if numero > 50 and numero % 7 == 0:
        print(f"Maior que 50 e divisível por 7: {numero}")
        break
        
        
