import os
os.system("cls || clear")

print("""
1 - cadastrar usuário
2 - excluir usuário
3 - sair do sistema
      """)

opcao = int(input("Digite uma opção: "))


match(opcao):
    case 1:
        print("Opção de cadastrar usuário")
    case 2:
        print("Opção de excluir usuário")
    case 3:2
    
        print("Opção de sair do sistema")
    case _:
        print("Opção inválida")

