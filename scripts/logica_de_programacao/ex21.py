# Contagem inteligente
ini = int(input("Inicio: "))
fim = int(input("Fim: "))


if ini < fim:
     while ini <= fim:
        print(ini)
        ini = ini + 1
else:
    while ini >= fim:
        print(ini)
        ini = ini - 1
