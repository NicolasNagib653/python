nome = input("Insira uma frase: ").strip()
print(f"""
      A palavra possui {nome.lower().count("a")} letras a
      A primeira letra a que aparece na posição: {nome.lower().find('a')}
      A última letra a aparece na posição: {nome.lower().rfind('a')}
      """)