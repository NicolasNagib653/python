preco    = float(input("Qual é o preço do produto? R$"))
desconto = preco - preco * (5/100)
print(f"O produto custava R${preco:.2f}, na promoção com desconto de 5% vai custar R${desconto:.2f}") 