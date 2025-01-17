nome = input("Insira seu nome: ")
sexo = input("Digite seu sexo(M,F): ").upper()
while sexo != "M" and sexo != "F":
    print("Você digitou um valor inexistente no sexo, os valores aceitos são: M ou F")
    sexo = input("Digite novamente seu sexo: ").upper()
print(f"Muito prazer {nome}!!!")
