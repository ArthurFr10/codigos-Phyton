import os
os.system("cls || clear")

#Solicitando dados
produto = float(input("Digite o valor do produto: "))

pagamento = int(input("""Digite o número correspondente a forma de pagamento:
1 - Pagamento à vista
2 - Pagamento à prazo
"""))

desconto = 0.10

desconto_final = produto * desconto
valor_final = produto - desconto_final
#Calculando
match(pagamento):
    case 1:
        print(f"Valor do produto: R${produto}")
        print(f"Forma de pagamento: À vista")
        print(f"Valor do desconto: R${desconto}:")
        print(f"Total a pagar: R${valor_final}")
        
    case 2:
       parcela = int(input("Digite a quantidade de parcelas que deseja parcelar(até 6x): "))
       valor_parcela = produto / parcela
       print(f"Valor do produto: R${produto}")
       print(f"Forma de pagamento: À prazo")
       print(f"Quantidade de parcelas: {parcela}")
       print(f"Valor por parcela: R${valor_parcela}")
       print(f"Total a prazo: R${produto}")
    case _:
        print("Opção inválida")

#Exibindo resultados

