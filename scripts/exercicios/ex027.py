nome = input("Insira seu nome: ")
tamn = len(nome.split()) -1

print(f"Primeiro nome {nome.split()[0]}")
print(f"Ultimo nome {nome.split()[tamn]}")