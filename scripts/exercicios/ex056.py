media = maior = menor =0
for i in range (1,5,1):
    print("-="*15)
    nome = input(f"Insira o nome da {i}º pessoa: ")
    idade = int(input(f"Insira a idade da {i}º pessoa: "))
    sexo = input(f"Insira o sexo da {i}º pessoa(f,m): ")
    print("-="*15, "\n")
    media += idade

    if idade > maior and sexo == "m":
        anoida = idade
        velho = nome
    if idade < 20 and sexo == "f":
        menor +=1


print(f"A média de idade do grupo é {media/4} anos")
print(f"O homem mais velho do grupo tem  anos {anoida} e se chama {velho}")
print(f"{menor} mulheres tem menos de 20 anos")