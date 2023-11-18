def ParOuImpar(v):
    if v%2 == 0:
        return "Par"
    else:
        return "impar"

n = int(input("Digite um número: "))
r = ParOuImpar(n)
print("O numero {} é um valor {}" .format(n,r))