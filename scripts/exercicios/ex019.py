import random

a1 = input("Insira o nome do primeiro aluno: ")
a2 = input("Insira o nome do segundo aluno: ")
a3 = input("Insira o nome do terceiro aluno: ")
a4 = input("Insira o nome do quarto aluno: ")
print(f"O nome do aluno sorteado é {random.choice([a1,a2,a3,a4])}")