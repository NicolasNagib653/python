n1   = int(input("insira um número inteiro: "))
print("""
      Para binário(bin)
      para octal(oct)
      para hexadecimal(hex)
""")
base = input("Escolha a base de conversão: ")
if base == "bin":
    print(f"{n1} convertido para BINÁRIO é igual a {bin(n1)[2:]}")
elif base == "oct":
    print(f"{n1} convertido para OCTAL é igual a {oct(n1)[2:]}")
elif base == "hex":
    print(f"{n1} convertido para HEXADECIMAL é igual a {hex(n1)[2:]}")
else:
    print("Opção inválida! Tente novamente")
