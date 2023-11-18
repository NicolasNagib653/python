soc = [1,2,3,4,5,6,7,8,9,10,11]
tot = 0
for i in range(1,11):
        nome = input("Digite seu nome:")
        palavras = nome.split()
        primeira_letra = palavras[0][:1]
        if primeira_letra == "c" or primeira_letra == "C":
            tot = tot +1
            soc[tot] = nome

print("Listagem final")
for i in range(tot):
      print(soc[i])
