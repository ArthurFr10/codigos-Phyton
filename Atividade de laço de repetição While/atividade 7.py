import os
os.system("cls || clear")


while True:
    senha = input("Crie uma senha: ")
    confirmacao_senha = input("Confirme sua senha: ")
    
    if senha == confirmacao_senha:
        print("Senha criada com sucesso!")
        break
    elif senha != confirmacao_senha:
        print("Tente novamente")



