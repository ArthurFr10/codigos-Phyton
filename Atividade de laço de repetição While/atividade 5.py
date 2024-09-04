import os
os.system("cls || clear")

contador = 0
codigo_certo = "PROMO2024"


while True:
    codigo = input("Digite um código de promoção: ")
    contador += 1
    print(f"Tentativa número: {contador}")
    if codigo == codigo_certo:
        print("Código aceito")
        print("Desconto recebido")
        break
    elif contador == 3:
        print("Opção inválida")
        break


    
    



