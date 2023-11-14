tot010 = 0
SImp   = 0
for i in range(6):
    v = int(input("Digite um valor: "))
    if v >= 0 and v <= 10:
        tot010 = tot010 +1
        if v%2 == 1:
            SImp = SImp + v

print("Ao todo foram {} valores entre 0 e 10" .format(tot010))
print("Nesse intervalo a soma de impares foi ", SImp)