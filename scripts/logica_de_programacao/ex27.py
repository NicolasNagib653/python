i = 1
n = int(input("Digite um valor: "))
contDiv = 0
while i <= n:
    if n % i == 0:
      contDiv = contDiv +1  
    i = i + 1
if contDiv > 2 :
   print("O valor {} não é primo" .format(n))
else:
   print("O valor {} é primo" .format(n))