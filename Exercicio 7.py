import os
os.system("cls || clear")

#Solicitando dados
semana = int(input("""

      Digite o número que representa o dia da semana: 
      1 - Domingo
      2 - Segunda
      3 - Terça
      4 - Quarta
      5 - Quinta
      6 - Sexta
      7 - Sábado             
     -> """))


#Calculando
match(semana):
    case 1:
        print("Final de semana")
    case 2:
        print("Dia útil")
    case 3:
        print("Dia útil")
    case 4:
        print("Dia útil")
    case 5:
        print("Dia útil")
    case 6:
        print("Dia útil")
    case 7:
        print("Final de semana")
    case _:
        print("Opção Inválida")

#Exibindo resultados
