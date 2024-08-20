import os 
os.system("cls || clear")  #Limpar o terminal

#Solicitando dados..
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
altura = float(input("Digite sua altura: "))

#Exibido resultados...

print(f"Nome: {nome}")
print(f"Idade: {idade}  anos.")
print(f"Altura: {altura} m.")

print(f"Meu nome é: {nome}, tenho {idade}, anos e {altura}m de altura.")
