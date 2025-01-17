salario = float(input("Qual o salário do Funcionário? R$"))
novo = salario + salario * 15/100
print(f"Um funcionário que ganhava R${salario}, com 15% de aumento, passa a receber R${novo:.2f}")