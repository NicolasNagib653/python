i=h=m= 0
while True:
    idade = int(input("Quantos anos a pessoa tem? "))
    sexo = input("Qual o sexo da pessoa[F/M]: ").upper()
    if idade > 18:
        i+=1
    if sexo == "M":
        h += 1
    if idade <20 and sexo =="F":
        m +=1
    res = input("Deseja continuar o cadastro? [S/N] ").upper()
    if res == "N":
        break
print(f"{i} pessoas possuem mais de 18 anos")
print(f"{h} homens foram cadastrados")
print(f"{m} mulheres possuem menos de 20 anos")