import os
os.system("cls || clear")



#Solicitando dados

nota = 0
while True:
    nota = float(input("Digite uma nota: "))

    if nota < 0 or nota > 10:
        print("\nA nota deve ser maior ou igual a zero ou menor ou igual a 10")
    else:
        break

print(f"Digite sua nota: {nota}")