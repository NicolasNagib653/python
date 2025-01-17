n1 = float(input("Insira um valor: "))
n2 = float(input("Insira outro valor: "))
print("""
    [1] soma
    [2] multiplicação
    [3] maior
    [4] novos números
    [5] sair do programa
""")
i  =  int(input("Escolha uma opção: "))
while i !=5:
    if i < 1 or i > 5:
        print("Opção inválida")
    elif i ==1:
        print(f"A soma entre {n1} e {n2} é {n1+n2}")
    elif i ==2:
        print(f"O produto entre {n1} e {n2} é {n1*n2}")
    elif i ==3:
        maior = 0
        if n1 > n2:
            print(f"O maior valor é: {n1}")
        else: 
            print(f"O maior valor é {n2}")
    elif i==4:
        n1 = float(input("Insira um valor: "))
        n2 = float(input("Insira outro valor: "))
        print("""
    [1] soma
    [2] multiplicação
    [3] maior
    [4] novos números
    [5] sair do programa
        """)
    i  =  int(input("Escolha uma opção: "))
print("Fim")        