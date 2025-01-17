maior = menor = 0
for i in range(1,6,1):
    peso = float(input(f"Insira o peso da {i}º pessoa(Kg): "))
    if peso > maior:
        maior = peso
    if menor == 0:
        menor = peso
    else:
        if peso < menor:
            menor = peso
print(f"O maior peso lido foi {maior}Kg e o menor peso lido foi {menor}Kg")