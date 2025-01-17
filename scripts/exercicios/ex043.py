peso = float(input("Qual é o seu peso(Kg)? "))
altura = float(input("Qual a sua altura(m)? "))
imc  = peso / altura**2
print(f"Seu IMC é de {imc:.1f}")

if imc < 18.5:
    print("\033[33mVocê está abaixo do peso!\033[37m")
elif imc <= 25:
    print("\033[32mVocê está com o peso ideal!\033[37m")
elif imc <= 30:
    print("\033[31mVocê está com sobrepeso!\033[37m")
elif imc <= 40:
    print("\033[31mVocê está com obesidade!\033[37m")
else:
    print("\033[31mVocê está com obesidade mórbida!\033[37m")