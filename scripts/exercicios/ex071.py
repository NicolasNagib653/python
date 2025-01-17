print("="*30)
print("{:^30}".format("BANCO DO NAGIB"))
print("="*30)

valor = int(input("Que valor você quer sacar? "))
cinq=vint=dez=um= 0
while True:
    if valor > 50:
        cinq +=1
        valor-=50
    elif valor > 20:
        vint +=1
        valor-=20
    elif valor > 10:
        dez +=1
        valor-=10
    elif valor >= 1:
        um +=1
        valor-=1
    else:
        break 
print(f"Total de {cinq} cédulas de R$50")
print(f"Total de {vint} cédulas de R$20")
print(f"Total de {dez} cédulas de R$10")
print(f"Total de {um} cédulas de R$1")
print("="*30)
print("Volte sempre!")