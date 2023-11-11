valor = 0
valor3 = 50

print("-------------------------------")
print("       Criança Esperança       ")
print("-------------------------------")
print("   Muito obrigado por ajudar   ")
print(" [1] para doar R$10")
print(" [2] para doar R$25")
print(" [3] para doar R$50")
print(" [4] para doar outros valores")
print(" [5] para cancelar")
d = float(input("n: "))

if(d == 1):
    valor = 10


elif(d == 2):
   valor = 25

elif(d == 3):
    valor = 50

elif(d == 4):
    valor = int(input("Qual o valor da doação? R$"))

else:
    valor = 0

print("-------------------------")
print(" Sua doação foi de R$", valor)
print(" Muito Obrigado!")
print("-------------------------")