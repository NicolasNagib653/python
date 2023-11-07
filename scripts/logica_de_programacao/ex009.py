ano_atua = int(input("Em que ano estamos? "))
ano_nasc = int(input("Em que ano você nasceu? "))
idade    = ano_atua - ano_nasc

print("Em", ano_atua, "Você terá ", idade, "anos")

if(idade >= 21) :{
    print("Você ja terá atingido a maior idade")
}
    
else :{
    print("Você ainda será menor de idade")
}
