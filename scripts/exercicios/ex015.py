dias = int(input("Por quantos dias o carro foi alugado? "))
km   = float(input("Quanto Km foi rodado? "))
valor = 60*dias + km*0.15
print(f"O total a pagar é {valor:.2f}")