import random
print("-="*20)
print("Vamos jogar par ou impar")
print("-="*20)
cont = 0
while True:
    n = int(input("Digite um valor: "))
    pi = input("Par ou impar? [P/I]: ").upper()
    if pi == "P":
        compPi = "I"
    elif pi == "I":
        compPi = "P"
    else:
        print("Erro!!")
    comp = random.randint(0,10)
    soma = n + comp
    print(f"O jogador jogou {n} e o computador jogou {comp} a soma é {soma}")
    if soma%2 == 0:
        if pi == "P":
            print("O jogador venceu!")
            cont+=1
        elif pi == "I":
            print("O computador venceu!")
            break
    elif soma%2 == 1:
        if pi == "P":
            print("O computador venceu!")
            break
        elif pi == "I":
            print("O jogador venceu!")
            cont+=1
print(f"O jogador venceu um total de {cont} vezes")