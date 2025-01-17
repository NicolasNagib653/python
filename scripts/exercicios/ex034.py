salario = float(input("Qual o seu salário? R$"))

if salario > 1250:
    print("Você recebeu um aumento de 10% no seu salário")
    print(f"Seu salário atual é de R${salario}")
    print(f"Seu salário com esse novo ajuste é R${salario + salario*10/100}")
else:
    print("Você recebeu um aumento de 15% no seu salário")
    print(f"Seu salário atual é de {salario}")
    print(f"Seu salário com esse novo ajuste é de R${salario + salario*15/100}")