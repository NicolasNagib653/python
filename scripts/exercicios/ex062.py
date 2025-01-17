c = int(input("Insira o início da PA: "))
p = int(input("Insira a razão da PA: "))

i = 0
while i <10:
    print(c)
    c +=p
    i+=1
termo = int(input("Deseja inserir mais quantos termos?"))
i=0 
while i < termo:
    print(c)
    c +=p
    i+=1
