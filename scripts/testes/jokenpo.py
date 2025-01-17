from random import randint
from time import sleep
import emoji

pedra = emoji.emojize(":raised_fist:", language="en")
papel = emoji.emojize(":hand_with_fingers_splayed:", language="en")
tesoura = emoji.emojize(":victory_hand:", language="en")
i = "S"
vitjog =vitcomp= 0

def verificar(n1):
    if n1 == 1:
        n2 = pedra
    elif n1 == 2:
        n2 = papel
    elif n1 == 3:
        n2 = tesoura
    else: 
        print("Opção inválida. Tente novamente")
    return n2
    
while i == "S":
        
    print("-="*20)
    print("Vamos jogar Jokenpô?")
    print("-="*20)

    print(f"""
        [ 1 ] para Pedra {pedra}
        [ 2 ] para Papel {papel}
        [ 3 ] para Tesoura {tesoura}
        """)
    jog = int(input("Qual a seu escolha? "))
    comp = randint(1,3)
    escolhajog  = verificar(jog)
    escolhacomp = verificar(comp)

    print("")
    print("Jo!")
    sleep(1)
    print("Ken!")
    sleep(1)
    print("PÔ!")
    sleep(1)

    print(f"Você escolheu {escolhajog}")
    sleep(0.5)
    print(f"O computador escolheu {escolhacomp}")
    sleep(0.5)

    if jog == comp:
        print(f"\033[33mEmpate\033[37m")
    elif (jog == 1 and comp == 3) or (jog == 2 and comp == 1) or (jog == 3 and comp == 2):
        print("Você \033[32mvenceu!\033[37m")
        vitjog +=1
    elif (jog == 1 and comp == 2) or (jog ==2 and comp == 3) or (jog == 3 and comp == 1):
        print("Você \033[31mperdeu!\033[37m")
        vitcomp +=1
        
    i = input("Você deseja jogar novamente? S/N: ").upper()
print("-="*20)
print(f"""
         Resultado final:
    \033[32mJogador {vitjog} \033[37mX \033[31m{vitcomp} Computador\033[37m
    """)
print("-="*20)

