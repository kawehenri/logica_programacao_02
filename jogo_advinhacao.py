import random
import os
import time

# recebe um número aleatório entre 0 e 100
numero_premiado = random.randint(0,100)
num_tentados = []
tentativas = 10
tempo = 30

os.system("cls")
while True:
    ent_usuario = int(input("Digite um número de 0 a 100: "))
    if ent_usuario == numero_premiado:
        print("Você ganhou.")
        num_tentados.append(ent_usuario)
        print(f"Número de tentativas: {len(num_tentados)}")
        print(f"Números tentados: {num_tentados}")
        break
    elif tentativas == 0:
        print(f"Você perdeu, o número premiado era {numero_premiado}")
    else:
        print("Você não acertou o número.")
        num_tentados.append(ent_usuario)
        tentativas -= 1
        if ent_usuario > numero_premiado:
            print("Digite um número menor")
        else:
            print("Digite um número maior")