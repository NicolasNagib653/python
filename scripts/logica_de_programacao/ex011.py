massa  = float(input("Qual o seu peso? "))
altura = float(input("A sua altura? "))
IMC    = round(massa / altura**2, 2)

print("O seu peso é de Kg", massa, "já a sua altura é de m", altura, "Seu IMC é", IMC)

if(IMC < 17):{
    print("Você está abaixo do peso")
}
    
elif((IMC >= 17) and (IMC <= 18.5)):{
    print("Abaixo do peso")
}
    
elif((IMC > 18.5) and (IMC <= 25)) :{
    print("Parabens você está com o peso ideal")
}
    
elif((IMC > 25) and (IMC <= 30)):{
    print("Sobrepeso")
}
    
elif((IMC > 30) and (IMC <= 35)):{
    print("Obesidade")
}
    
elif((IMC > 35) and (IMC <= 40)):{
    print("Obesidade severa")
}
    
else:{
    print("Obesidade mórbida")
}