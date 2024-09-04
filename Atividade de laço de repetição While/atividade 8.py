import os
os.system("cls || clear")

total_estudado = 0
meta = int(input("Digite uma meta de horas de estudos: "))
while True:
    horas_estudadas = int(input("Digite as horas estudadas: "))
    total_estudado += horas_estudadas
    if total_estudado >= meta:
        print(f"meta de horas: {meta} horas")
        print(f"Total de horas estudadas: {total_estudado} horas")
        break


