import os
# Definindo listas vazias para armazenar os dados dos usuários
nomes = []
idades = []
alturas = []
pesos = []
sobrenomes = []

# Função sem retorno.
def logoSenai():
    os.system("cls || clear")
    print("=== SENAI === ")

# Solicitando os dados dos usuários em um loop
while True:
    logoSenai()
    nome = input("Digite o nome do usuário (ou digite 'sair' para encerrar): ")
    
    # Verificando se o usuário quer sair
    if nome.lower() == 'sair':
        break
    
    sobrenome = input("Digite seu sobrenome: ")
    idade = int(input("Digite a idade do usuário: "))
    altura = float(input("Digite a altura do usuário (em metros): "))
    peso = float(input("Digite o peso do usuário (em quilogramas): "))
    
    # Adicionando os dados às listas
    nomes.append(nome)
    idades.append(idade)
    alturas.append(altura)
    pesos.append(peso)
    sobrenomes.append(sobrenome)

#Funções com retorno
def calculo_imc(a,b):
    lista_imc = []
    for i,peso in enumerate(a):
        imc = peso/ b[i] **2
        lista_imc.append(imc)
    return lista_imc

lista_imc = calculo_imc(pesos, alturas)

def interpretando_imc(a):
    interpretacoes = []
    for numero in a:
        if numero < 18.5:
            interpretacoes.append("Abaixo do peso")
        elif numero >= 18.5 and numero < 25:
            interpretacoes.append("Peso normal")
        elif numero >= 25 and numero < 30:
            interpretacoes.append("Sobrepeso")
        elif numero >= 30 and numero < 35:
            interpretacoes.append("Obesidade grau I")
        elif numero >=35 and numero < 40:
            interpretacoes.append("Obesidade grau II")
        elif numero >= 40:
            interpretacoes.append("Obesidade grau III")
    return interpretacoes

interpretacoes = interpretando_imc(lista_imc)




# Exibindo os dados armazenados
logoSenai()
print("\nDados dos usuários:")
for i in range(len(nomes)):
    print("="*20)
    print(f"Usuário {i+1}:")
    print("Nome:", nomes[i], sobrenomes[i])
    print("Idade:", idades[i], "anos")
    print("Altura:", alturas[i], "metros")
    print("Peso:", pesos[i], "quilogramas")
    print(f"IMC: {lista_imc[i]:.2f}")
    print("Situação:", interpretacoes[i])
    