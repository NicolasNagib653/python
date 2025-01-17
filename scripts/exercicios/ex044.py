print("============== Lojas Nagib ==============")
preco = float(input("Preço das compras: R$"))
print("""
Formas de pagamento:
[1] à vista dinheiro ou cheque
[2] à vista cartão
[3] 2X no cartão
[4] 3X ou mais no cartão
      """)
opcao = int(input("Qual é a opção? "))
if opcao == 1:
    desconto = preco - preco * 10/100
    print(f"O valor da sua compra é de R${preco:.2f}, com o desconto aplicado o valor é de R${desconto:.2f}")
elif opcao == 2:
    desconto = preco - preco *5/100
    print(f"O valor da sua compra é de R${preco:.2f}, com o desconto aplicado o valor é de R${desconto:.2f}")
elif opcao == 3:
    print(f"O valor da sua compra é de R${preco:.2f}, e o valor das parcelas é de R${(preco/2):.2f}")
elif opcao == 4:
    parcelas = int(input("Quantas parcelas vão ser? "))
    juros = preco + preco * 20/100
    print(f"O valor atual é de R${preco:.2f}, com o juros aplicado o valor passa a ser deR${juros:.2f} e o valor de cada parcela é de R${(juros/parcelas):.2f} ")
else:
    print("Opção inválida, tente novamente")