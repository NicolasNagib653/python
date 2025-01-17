import math

alpha = int(input("Insira um angulo: "))
rad   = math.radians(alpha) #Converte o valor digitado para radianos
print(f"O valor do seno é {math.sin(rad):.2f} o do cosseno é {math.cos(rad):.2f} e a tangente é {math.tan(rad):.2f}")