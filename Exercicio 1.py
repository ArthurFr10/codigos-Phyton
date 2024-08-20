import os 

os.system("cls || clear")

#Solicitando dados
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
primeira_nota = float(input("Digite sua primeira nota: "))
segunda_nota = float(input("Digite sua segunda nota: "))
terceira_nota = float(input("Digite sua terceira nota: "))
media = (primeira_nota + segunda_nota + terceira_nota) / 3

if media < 7:
    print(f"O aluno será reprovado")
else:
    print(f"O aluno sera aprovado")


#Verificando
print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"primeira nota: {primeira_nota}")
print(f"Segunda nota: {segunda_nota}")
print(f"Terceira nota: {terceira_nota}")
print(f"Média: {media}")

