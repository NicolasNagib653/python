frase = input("Insira uma frase: ").split()
frase = "".join(frase)
tam = len(frase)
cont = 0
fraseinv = ""
for i in range(0,tam):
    if frase[i] == frase[tam-1]:
        cont += 1
    tam -=1
    fraseinv += frase[tam]
print(f"O inverso de {frase} é {fraseinv}")
if cont == len(frase):
    print("A frase é um palíndromo")
else:
    print("A frase não é um palíndromo")