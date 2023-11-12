r = "s"
h = 0
m = 0
while r == "s":
    print("======================")
    print("  Seletor de pessoas  ")
    print("======================")

    s = input("Qual o sexo? [m/f] ")
    i = int(input("Qual a idade? "))
    print("Qual a cor do cabelo? ")
    print("---------------------")

    print("[1] Preto")
    print("[2] Castanho")
    print("[3] Loiro")
    print("[4] Ruivo")
    cor = input("qual? ")

    if i >= 18 and cor == "2" and s == "m":
        h = h + 1
    elif  i >= 25 and i <= 30 and cor == "3" and s == "f":
        m = m + 1
    r = input(" Quer continuar? [s/n] ")
print("Total de homens com mais de 18 e cabelos castanhos {}" .format(h))
print("Total de mulheres entre 25 e 30 e cabelos loiros", m)