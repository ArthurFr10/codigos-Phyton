import os
os.system("cls || clear")

orcamento = 100
gasto_mensal = 0
print(f"Orçamento: {orcamento} reais")
while True:
    gasto_inicial = int(input("Digite seus gastos: "))
    gasto_mensal += gasto_inicial
    print(f"Gastos já acumulados: {gasto_mensal}")
    if gasto_mensal > orcamento:
        print(f"Total gasto: {gasto_mensal} reais")
        break43255