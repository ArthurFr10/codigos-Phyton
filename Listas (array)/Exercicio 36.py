import os
os.system("cls || clear")

#Entrada
QUANTIDADE_NOTA = 5
lista_numero = []

print("\n === Solicitando dados === ")
for i in range(QUANTIDADE_NOTA):
    numero = float(input(f"Digite o {i+1}ª número: "))
    lista_numero.append(numero)


#Processamento

maior_numero = max(lista_numero)
menor_numero = min(lista_numero)

#Saída

print("\n=== Exibindo resultados ===")
for contador, nota in enumerate(lista_numero):
    print(f"{contador + 1}ª nota: {nota}")

print(f"\nMenor número: {menor_numero}")
print(f"Maior número: {maior_numero}")