i    = 1
totN = 0

while i <= 5:
    n = int(input("Digite um numero: "))
    if n < 0 :
        totN = totN + 1
    i = i + 1
print("Foram digitados {} numeros negativos" .format(totN))