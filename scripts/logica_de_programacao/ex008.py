# Calculo de valor de um empréstimo com uma taxa de 20% de juros

emprestimo = float(input("Qual o valor do empréstimo? "))
numero_parcelas = int(input("Qual o número de parcelas? "))
juros      = emprestimo * 20 / 100
emprestimo_juros = emprestimo + juros
parcelas   = emprestimo_juros / numero_parcelas

print("O valor do emprestimo é de R$", emprestimo)
print("O valor do juros do emprestimo é de R$", juros)
print("O valor do emprestimo com o juros é de R$", emprestimo_juros)
print("O número de parcelas é de", numero_parcelas)
print("O valor de cada parcela será de R$", parcelas)