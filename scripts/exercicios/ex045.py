from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)
print('''Suas opções:
[0] Pedra
[1] Papel
[2] Tesoura
''')
jogador = int(input("Qual é a sua jogada? "))
print("Jo!")
sleep(1)
print("Ken!")
sleep(1)
print("Pô!!!")
sleep(1)
print("-="*11)
print(f"computador jogou {itens[computador]}")
print(f"Jogador jogou {itens[jogador]}")
print("-="*11)

if computador == 0: #Computador jogou Pedra
    if jogador == 0:
        print("Empate!")
    elif jogador == 1:
        print("Jogador vence!")
    elif jogador == 2:
        print("Computador vence!")
    else:
        print("Jogada invállida")
elif computador == 1: #Computador jogou Papel
    if jogador == 0:
        print("Computador vence")
    elif jogador == 1:
        print("Empate!")
    elif jogador == 2:
        print("O jogador vence")
    else:
        print("Jogada invállida")
elif computador == 2: #Computador jogou Tesoura
    if jogador == 0:
        print("O jogador vence")
    elif jogador == 1:
        print("O computador vence")
    elif jogador == 2:
        print("Empate!")
    else:
        print("Jogada invállida")