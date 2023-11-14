sompar = 0
soma  = 0
divcin  = 0
nulo  = 0

for i in range(1,6):
    valor = int(input("Digite o {}o. Valor: " .format(i)))
    soma = soma + valor
    media = soma / 5
    if valor%5 == 0:
        divcin = divcin + 1
    if valor%2 == 0:
        sompar = sompar + valor
    if valor == 0:
        nulo = nulo + 1
print("A soma entre os valores é ", soma)
print("A media entre os valores é ", media)
print("Valores divisiveis por cinco: ", divcin)
print("Valores nulos: ", nulo)
print("A soma dos valores pares é ", sompar)