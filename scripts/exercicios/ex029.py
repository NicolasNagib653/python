velo = int(input("Insira a velocidade do carro: "))
multa = (velo - 80) * 7

print(f"Sua velocidade é de {velo}Km/h")
if velo > 80:
    print("Você está acima da velocidade permitida!")
    print(f"Sua multa é de R${multa}")
else:
    print("Você está na velocidade permitida")