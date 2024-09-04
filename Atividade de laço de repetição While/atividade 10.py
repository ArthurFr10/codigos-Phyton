import os
os.system("cls || clear")

soma_calorias = 0
limite_calorias = 2000
print(f"Limite de calorias para consumir: {limite_calorias}")
while True:
    calorias = int(input("Digite a quantidade de calorias consumidas: "))
    soma_calorias += calorias
    excesso_calorias = soma_calorias - limite_calorias
    if soma_calorias > limite_calorias:
        break

print(f"Total de calorias: {soma_calorias}")
print(f"Excesso de calorias: {excesso_calorias}")