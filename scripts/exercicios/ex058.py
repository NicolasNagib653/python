import random

n1 = int(input("Descubra o número escolhido pelo computador de 1 a 10: "))
n2 = random.randint(1,10)
palpites = 1
while n1 != n2:
    print("Você errou!")
    n1 = int(input("Tente novamente: "))
    palpites+=1
print(f"O número escolhido pelo computador foi: {n2} e foram necessários {palpites} palpites até você acertar")
