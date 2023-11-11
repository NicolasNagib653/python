# Contagem inteligente
ini = int(input("Inicio: "))
fim = int(input("Fim: "))


if(ini < fim):
     while ini <= fim:
        print(ini)
        ini = ini + 1
elif(ini > fim):
    while fim <= ini:
        print(fim)
        fim = fim - 1
print("Acabou")