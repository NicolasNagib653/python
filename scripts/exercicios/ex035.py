a = int(input("Insira o valor do primeiro lado do triangulo: "))
b = int(input("Insira o valor do segundo lado do triangulo: "))
c = int(input("Insira o valor do terceiro lado do triangulo: "))

if b-c < a < b+c and a-c < b < a+c and a-b < c < a+b:
    print("O triângulo é verdadeiro!")
else:
    print("O triângulo não é real!")