import os
os.system("cls || clear")

#Solicitando dados
print("""
      1 - Picanha - R$25,00
      2 - Lasanha - R$20,00
      3 - Strogonoff - R$18,00
      4 - Bife Acebolado - R$15,00
      5 - Pão com ovo - R$5,00  
""")

codigo_prato = int(input("Digite o número correspondente ao prato: "))


#Calculando


match(codigo_prato):
    case 1:
        print("Picanha - R$25,00")
    
    case 2:
        print("Lasanha - R$20,00")
    
    case 3:
        print("Strogonoff - R$18,00")
    
    case 4:
        print("Bife acebolado - R$15,00")
    
    case 5:
        print("Pão com ovo - R$5,00")
    case _:
        print("Opção inválida")
        


#Exibindo resultados
