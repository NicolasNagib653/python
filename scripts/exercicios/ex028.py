import random

n1 = int(input("Descubra o número escolhido pelo computador de 1 a 5: "))
n2 = random.randint(1,5)
if n1 == n2:
    print("Você ganhou!")
else:
    print("Você Perdeu!")

print(f"O número escolhido pelo computador foi: {n2}")