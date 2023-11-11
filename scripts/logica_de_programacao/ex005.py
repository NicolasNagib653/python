# Conversor de Real para Dólar com base em uma taxa fixa de U$4.89
i = 1
q = int(input("Qunatas vezes você quer converter? "))
while (i <= q):
    dinheiroR = float(input("Quantos reais eu tenho? "))
    dinheiroD = round(dinheiroR / 4.89, 2)
    print("O valor aproximado em doláres seria", dinheiroD)
    i = i + 1
    