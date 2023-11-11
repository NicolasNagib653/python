print("---------------------------")
print("   Escola Javali Cansado   ")
print("---------------------------")

nota1 = float(input("Primeira nota "))
nota2 = float(input("Segunda nota "))
media = (nota1 + nota2) /2


if(media > 9):
    print("Aluno nota A")
    print("Media: ", media)
elif(media > 8) and (media <= 9):
    print("Aluno nota B")
    print("Media: ", media)
elif(media > 7) and (media <= 8):
    print("Aluno nota C")
    print("Media: ", media)
elif(media > 6) and (media <= 7):
    print("Aluno nota E")
    print("Media: ", media)
else:
    print("Aluno nota F")
    print("Media: ", media)
