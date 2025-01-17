soma = prodCaro = 0
nomeProd = input("Qual o nome do produto? ")
precProd = float(input("Qual o preço do produto? "))
menor = precProd
prodBarato = ""
res = input("Deseja continuar[S/N]? ").upper()
while True:
    nomeProd = input("Qual o nome do produto? ")
    precProd = float(input("Qual o preço do produto? "))
    soma += precProd
    if precProd > 1000:
        prodCaro += 1
    if precProd < menor:
        prodBarato = nomeProd
    res = input("Deseja continuar[S/N]? ").upper()
    if res != "S":
        break
print(f"O preço total da compra é: R${soma}")
print(f"{prodCaro} produtos custam mais que R$1000")
print(f"O produto mais barato foi: {prodBarato}")
    