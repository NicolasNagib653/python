val = [1,2,3,4,5,6,7,8,9,10]
TotPar = 0

for i in range(1,8):
    val[i] = int(input("Digite o {}o. valor: " .format(i)))



for i in range(1,8):
    if val[i]%2 == 0:
        TotPar = TotPar + 1
        print("Valor par na posição", i)

print("O total de pares foi", TotPar)