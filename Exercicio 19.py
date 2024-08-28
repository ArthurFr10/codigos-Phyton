"""
Crie um programa que solicite ao usuário seu login e uma senha

O programa deve continuar pedindo o login e a senha até que ambos estejam corretos
"""
import os
os.system("cls || clear ")


#Solcitando dados
login_salvo = "arthur"
senha_salva = "123"
login = input("Digite seu login: ")

senha = input(("Digite sua senha: "))

while True:
    if login == login_salvo and senha == senha_salva:
        print("Bem vindo")
    else:
        print("Tente Novamente")
    break




#Calculando


#Exibindo resultados

