from math import sqrt

cata = float(input("Insira o valor do cateto adjacente: "))
cato = float(input("Insira o valor do cateto oposto: "))
hip  = sqrt((cata**2) + (cato**2))
# outro método math.hypot(cata, catb)
print(f"O valor da hipotenusa é {hip:.2f}")