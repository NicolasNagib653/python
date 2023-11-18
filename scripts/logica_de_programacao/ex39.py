def soma(a,b):
    s = a + b
    return s
v1 = int(input("Digite o primeiro valor: "))
v2 = int(input("Digite o segundo valor: "))
res = soma(v1,v2)
print("A soma entre {} e {} é igual a {} " .format(v1, v2, res))