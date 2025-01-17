nome = input("Qual é o seu nome?")

if nome == "Nicolas":
    print("Que nome bonito!")
elif nome == "Pedro":
    print("Seu nome é bem popular no Brasil.")
elif nome in "Ana":
    print("Belo nome feminino")
else:
    print("Que nome normal.")
print(f"Tenha um bom dia, {nome}!")