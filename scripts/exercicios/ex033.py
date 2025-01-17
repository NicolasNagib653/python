n1 = int(input("Insira um número: "))
n2 = int(input("Insira outro número: "))
n3 = int(input("Insira outro número: "))
menor = n1
maior = n1
if n2<n1 and n2<n3:
    menor = n2
if n3<n1 and n3<n2:
    menor = n3
print(f"O menor valor é {menor}")

if n2>n1 and n2>n3:
    maior = n2
if n3>n1 and n3>n2:
    maior = n2
print(f"O maior valor é {maior}")