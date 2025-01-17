n1 = int(input("Insira um número: "))
primo = 0
for i in range(1,n1+1):
    if n1%i == 0:
        primo +=1
        print(f"\033[33m{i}\033[m")
    else:
        print(i) 
if primo == 2 or n1 == 1:
    print("Ele é primo")
else:
    print("Não é primo")