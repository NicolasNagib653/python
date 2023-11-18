def Fatorial(v):
    c = 1
    r = 1
    v = v + 1
    for i in range(1,v):
        r = r * c
        c = c + 1
    return r

n = int(input("Digite um número: "))
f = Fatorial(n)
print("O valor de {}! é igual a {}" .format(n,f))