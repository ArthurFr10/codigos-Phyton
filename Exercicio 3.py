import os
os.system("cls || clear")
#Solicitando dados

login = input("Digite seu login: ")
senha = int(input("Digite sua senha: "))
#Exibindo resultados

if login == "arthur" and senha == 123:
    print("Bem-Vindo!")
else:
    print("Login ou senha inválidos")
        