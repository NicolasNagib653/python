n1 = int(input("Insira um valor: "))
fat = 1
i = n1
while i > 0:
    fat *= i
    i -=1
print(f"O fatorial de {n1} é: {fat}")