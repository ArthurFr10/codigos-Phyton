import os
os.system("cls || clear")

#####REFAZER CODIGO 

#Entrada
QUANTIDADE_NOTA = 6
lista_numero = []
print("\n === Solicitando dados === ")
for i in range(QUANTIDADE_NOTA):
    numero = float(input(f"Digite o {i+1}ª número: "))
    lista_numero.append(numero)


#Processamento

def par_impar(a):
    par = a
    impar = a
    contador = 2
    contador2 = 0
    if par % 2 == 0:
        contador += 1

    elif impar % 2 != 0: 
        contador2 += 1 
    return contador, contador2
    

pares, impares= par_impar(numero)
    

    

#Saída

print("\n=== Exibindo resultados ===")

print(pares)
print(impares)
