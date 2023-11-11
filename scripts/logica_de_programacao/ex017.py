print("-----------------------")
print("   Brasil X Alemanha   ")
print("-----------------------")

Time1 = int(input("Quantos gols o Brasil fez? "))
Time2 = int(input("Qunatos gols a Alemanha fez? "))
Difer = Time1 - Time2
Dife1 = abs(Difer)


if(Dife1 >= 4):
    print("Gols do Brasil ", Time1)
    print("Gols da Alemanha ", Time2)
    print("Diferença de gols", Dife1)
    print("Resultado: Goleada")
    
elif(Dife1 <= 4) and (Dife1 > 0):
    print("Gols do Brasil ", Time1)
    print("Gols da Alemanha ", Time2)
    print("Diferença de gols", Dife1)
    print("Resultado: Partida normal")

else:
    print("Gols do Brasil ", Time1)
    print("Gols da Alemanha ", Time2)
    print("Diferença de gols", Dife1)
    print("Resultado: Empate")
