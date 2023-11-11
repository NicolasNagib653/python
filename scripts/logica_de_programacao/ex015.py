nome =       input("Qual o nome do funcionario? ")
sal  = float(input("Qual o salário do funcionario? R$"))
dep  = int  (input("Qual a quantidade de dependentes? "))

if(dep == 0):
    Nsal = round(sal + (sal*5/100), 2)

elif(dep == 1) or (dep == 2) or (dep == 3):
    Nsal = round(sal + (sal*10/100), 2)
elif(dep == 4) or (dep == 5) or (dep == 6):
    Nsal = round(sal + (sal*15/100), 2)
else:
    Nsal = round(sal + (sal*18/100), 2)

print("O novo salario de ", nome, " sera de R$", Nsal)