l1 = float(input("Digite o primeiro lado "))
l2 = float(input("Digite o segundo lado "))
l3 = float(input("Digite o terceiro lado "))

Tri = (l1 < l2 + l3) and (l2 < l1 +l3) and (l3 < l1 + l2)
Eq = (l1 == l2) and (l2 == l3)
Es = (l1 != l2) and (l2 != l3) and (l1 != l3)


print("Pode formar um triangulo?", Tri)
print("O triangulo é equilátero?", Eq)
print("O triangulo é escaleno?", Es)