import os
os.system("cls || clear")


peso = float(input("Digite seu peso(Kg): "))
altura = float(input("Digite sua altura(m): "))

def calculo(num1, num2):
    imc = num1 / (num2 ** 2)
    if imc < 18.5:
        print("Abaixo do peso")
        print("Consulte um nutricionista para orientação")
    elif imc >= 18.5 and imc <= 24.9:
        print("Peso Normal")
        print("Mantenha hábitos saudáveis")
    elif imc >= 25 and imc <= 29.9:
        print("Sobrepeso")
        print("Considere uma dieta balanceada e atividade física")
    elif imc >= 30 and imc <= 34.9:
        print("Obesidade grau 1")
        print("Procure orientação de um profissional de saúde")
    elif imc >= 35 and imc <= 39.9:
        print("Obesidade grau 2")
        print("Consulte um médico para avaliação e orientação")
    elif imc >= 40:
        print("Obesidade grau 3")
        print("Busque assistência médica imediatamente")
    return imc

imc = calculo(peso, altura)
print(f"IMC: {imc:.2f}")

