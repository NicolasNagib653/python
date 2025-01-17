from datetime import date

datnas = int(input("Ano de nascimento: "))
ano    = date.today().year
idade  = ano - datnas
print(f"Quem nasceu em {datnas} tem {idade} anos em {ano}")

if idade < 18:
    print(f"Ainda faltam {18 - idade} anos para o alistamento")
    print(f"Seu alistamento será em {ano + 18 - idade}")
elif idade > 18:
    print(f"Você ja deveria ter se alistado há {idade - 18} anos")
    print(f"Seu alistamento foi em {ano + 18 - idade}")
else:
    print("Você tem que se alistar IMEDIATAMENTE")