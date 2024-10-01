import os
from dataclasses import dataclass

os.system("cls || clear")

#Estrutura de dados

@dataclass
class Cliente:
    nome: str
    sobrenome: str
    idade: int
    peso: float
    altura: float

QUANTIDADE_CLIENTES = 4

lista_de_clientes = []

print("\n === Solicitando dados dos clientes ===")
for i in range(QUANTIDADE_CLIENTES):
    cliente = Cliente(
        nome = input ("Digite seu nome: "),
        idade = int(input("Digite sua idade: ")),
        sobrenome = str(input("Digite seu sobrenome: ")),
        peso = float(input("Digite seu peso: ")),
        altura = float(input("Digite sua altura: "))       
    )
    lista_de_clientes.append(cliente)

print("=== Exibindo dados de um cliente ===")
#Salvar em um arquivo chamado: carteira_de_clientes.txt
nome_arquivo = "carteira_de_clientes.txt"

#Fazer leitura de dados do arquivo carteira_de_clientes.txt e mostre o terminal
with open(nome_arquivo, "a") as arquivo_cliente:
    for cliente in arquivo_cliente:
        arquivo_cliente.write(f"{cliente.nome}, {cliente.idade}, {cliente.sobrenome}, {cliente.peso}, {cliente.altura}\n")
    
arquivo_cliente.close()



