print("-="*20)
print("Analisador de triângulos 2.0")
print("-="*20)

a = int(input("Insira um valor do lado A de um triângulo: "))
b = int(input("Insira um valor do lado B de um triângulo: "))
c = int(input("Insira um valor do lado C de um triângulo: "))

if b-c < a < b+c and a-c < b < a+c and a-b < c < a+b:
    print("Os segmentos podem formar um triângulo ", end="")
    if a == b == c:
        print("equilátero")
    elif a == b or a == c or b == c:
        print("isósceles")
    else:
        print("escaleno")
else:
    print("Os segmentos não podem formar um triângulo!!!")