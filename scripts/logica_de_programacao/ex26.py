
r = "s"
while r =="s":
    f = 1 
    n = int(input("Digite um numero: "))
    i = n
    while i >= 1: 
        f = f * i
        i = i -1
    print("Valor de fatorial de {} é igual a {}" .format(n,f))
    r = input("Você quer continuar? [s/n]")
print("Fim do programa")