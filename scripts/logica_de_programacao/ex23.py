
s = 0
resp = "s"
while resp == "s":
    n = int(input("Digite um valor:"))
    s = s + n
    resp = input("Você quer continuar? [s/n] ")
print("A soma de todos os valores foi", s)
