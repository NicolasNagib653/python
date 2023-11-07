ano_atua = int(input("Ano Atual (YYYY): "))
ano_nasc = int(input ("Ano de nascimento (YYYY): "))
idade    = ano_atua - ano_nasc

print("Idade: ",idade)
if(idade < 18):{
    print("Inapto a tirar carteira")
}
else :{
    print("Apto a tirar carteira")
}