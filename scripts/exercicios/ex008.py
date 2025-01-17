medida = float(input("Uma distância em metros: "))

print("A medida de {:,1f}m corresponde a".format(medida))
print("{}Km".format(medida/1000))
print("{}hm".format(medida/100))
print("{}dam".format(medida/10))
print("{}dm".format(medida*10))
print("{}cm".format(medida*100))
print("{}mm".format(medida*1000))