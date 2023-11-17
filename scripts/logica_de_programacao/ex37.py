n = int(input("Digite um número: "))

def ParOuImpar(V):
    if V % 2 == 0:
        print("O número {} é par" .format(V))
    else:
        print("O número {} é impar" .format(V))

ParOuImpar(n)