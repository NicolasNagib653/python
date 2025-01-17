res = "S"
n2=maior= soma=menor = 0
while res == "S":
    n = int(input("insira um valor: "))
    soma += n
    n2 +=1
    if n > maior:
        maior = n
    else:
        menor = n
    res = input("Deseja inserir outro valor? S/N: ").upper()
print(f"A media entre os valores digitados é : {soma/n2}")
print(f"O maior valor digitado foi: {maior}")
print(f"O menor valor digitado foi: {menor}")