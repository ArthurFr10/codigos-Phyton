"""
Crie um programa que solicite ao usuário seu login e uma senha
O programa deve continuar pedindo o login e a senha até que ambos estejam corretos
O programa deve solicitar o login e senha apenas três vezes
Caso ultrapasse o número de tentativas, o programa deve ser finalizado
"""
import os
os.system("cls || clear ")

login_salvo = "arthur"
senha_salva = "123"
contador = 0



while True:
    login = input("Digite seu login: ")
    senha = input(("Digite sua senha: "))
    contador += 1
    
    if login == login_salvo and senha == senha_salva:
            print("Bem vindo")
            break
    else:
            print(f"Tentativa: {contador} \n")
            print("Login ou senha inválidos")
            if contador == 3:
                   break


