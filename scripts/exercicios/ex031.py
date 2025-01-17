distancia = int(input("Qual a distância da sua viagem? "))

if distancia <= 200:
    print(f"Sua viagem vai ser de {distancia}Km, então o valor dela vai ser de R${distancia * 0.50}")
else:
    print(f"Sua viagem vai ser de {distancia}Km, então o valor dela vai ser de R${distancia * 0.45}")