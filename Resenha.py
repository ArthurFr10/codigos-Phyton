import os
os.system("cls || clear")

#Solicitando dados
time = int(input("""
      Digite o melhor time do brasil:  
      
      1 - Palmeiras
      2 - Flamengo
      3 - Bahia
      4 - Grêmio
      5 - São paulo
      
      ->  """))



match(time):
    case 1:
        print("Opção incorreta")
        print("TENTE NOVAMENTE")
    case 2:
        print("Opção incorreta")
        print("TENTE NOVAMENTE")
    case 3:
        print("BORA BAHIA MINHA PORRA!")
    case 4:
        print("Opção incorreta")
        print("TENTE NOVAMENTE")
    case 5:
        print("Opção incorreta")
        print("TENTE NOVAMENTE")
    case _:
        print("Digite uma opção válida!")
#Calculando

#Exibindo resultados
