from datetime import date
datnasc = int(input("Ano de nascimento: "))
ano = date.today().year
idade = ano - datnasc

print(f"O atleta possui {idade} anos")
if idade <= 9:
    print("O atleta é MIRIM")
elif 14 >= idade > 9:
    print("O atleta é INFANTIL")
elif 19 >= idade > 14:
    print("O atleta é JUNIOR")
elif 25 >= idade > 19:
    print("O atleta é SÊNIOR")
else:
    print("O atleta é MASTER")