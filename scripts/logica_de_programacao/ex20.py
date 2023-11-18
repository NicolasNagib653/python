cont = 1
s = 0
maior = 0
menor = 0
while cont <= 5:
    n = int(input("Digite um valor:"))
    if (n > maior):
        maior = n
    else: 
        menor = n
    s = s + n
    cont = cont + 1
print("A soma de todos os valores foi", s)
print("O maior número digitado foi ", maior)
print("O menor número digitado foi ", menor)