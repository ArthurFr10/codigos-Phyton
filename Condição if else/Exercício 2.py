import os
os.system("cls || clear")

#Solicitando dados...
nome = input("Digite seu nome: ")
primeiro_numero = float(input("Digite o primeiro número: "))
segundo_numero = float(input("Digite o segundo número: "))


#calculando
soma = primeiro_numero + segundo_numero
produto = primeiro_numero * segundo_numero
media = (primeiro_numero + segundo_numero) / 2
if primeiro_numero > segundo_numero:
    menor_numero = segundo_numero
else:
    menor_numero = primeiro_numero

if segundo_numero > primeiro_numero:
    maior_numero = segundo_numero
else:
    maior_numero = primeiro_numero

#Exibindo resultados
print(f"Nome: {nome}")
print(f"Soma: {soma}")
print(f"Produto: {produto}")
print(f"média: {media}")
print(f"Menor valor: {menor_numero}")
print(f"Maior valor: {maior_numero}")