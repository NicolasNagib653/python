n = int(input("insira um valor: "))
dig=soma= 0
while n !=999:
    n = int(input("insira outro valor: "))
    dig += 1
    soma += n
print(f"Foram digitados {dig} números, e a soma de todos eles é: {soma - 999}")