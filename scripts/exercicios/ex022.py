nome = input("Qual o seu nome? ")
tam  = nome.split()
tam  = len(''.join(tam))
print(f"""
          Seu nome com todas as letras maiúsculas: {nome.upper()}
          Seu nome com todas as letras minúsculas: {nome.lower()}
          Seu nome possui {tam} letras
          O seu primeiro nome é {nome.split()[0]} possui {len(nome.split()[0])} letras""")
