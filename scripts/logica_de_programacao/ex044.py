nome = [1,2,3,4,5]
n1   = [1,2,3,4,5]
n2   = [1,2,3,4,5]
m    = [1,2,3,4,5]
sm   = 0
tot  = 0
for i in range(1,5):
        print("Aluno ", i)
        nome[i] = input("Nome: ")
        n1[i] = float(input("Primeira Nota: "))
        n2[i] = float(input("Segunda Nota: "))
        m[i] = (n1[i] + n2[i])/2
        sm = sm + m[i]
mt = sm/4

print("Listagem de alunos")
print("-----------------------")
for i in range(1,5):
        print(nome[i],"             ", m[i])
        if m[i] > mt:
            tot = tot + 1
print("Ao todo temos {} alunos acima da media da turma que é {}" .format(tot,mt))

