valcas = float(input("Valor da casa: R$"))
sala   = float(input("Salário do comprador: R$"))
ano    = int(input("Quantos anos de financiamento? "))
mensal = ano * 12
prest  = valcas / mensal
valor  = sala * 30/100

print(f"Para pagar uma casa de {valcas} em {ano} anos, a prestação será de R${prest:.2f}")

if prest <= valor:
    print("\033[32mEmpréstimo APROVADO!\033[37m")
else:
    print("\033[31mEmpréstimo NEGADO!\033[37m")