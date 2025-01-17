from datetime import date
maior = menor =0
ano = date.today().year
for i in range(1,8,1):
    anonasc = int(input(f"Insira o ano de nascimento da pessoa nº{i}: "))
    if int(ano)-anonasc >= 21:
        maior +=1
    else:
        menor +=1
print(f"{maior} pessoas já atingiram a maior idade")
print(f"{menor} pessoas ainda não atingiram a maior idade")