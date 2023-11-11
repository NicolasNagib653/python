# Calculo de media
print("ESCOLA JAVALI CANSADO")

nota1 = float(input("Primeira nota: "))
nota2 = float(input("Segunda nota: "))
nota3 = float(input("Terceira nota: "))
nota4 = float(input("Quarta nota: "))
media = round((nota1 + nota2 + nota3 + nota4) /4, 1)

print("Media: ", media)
if(media >= 7) :{
    print("Aluno aprovado")
}
elif ((media >= 5) and (media <7)):{
    print("Aluno em recuperação")
}
else :{
    print("Aluno reprovado")
}