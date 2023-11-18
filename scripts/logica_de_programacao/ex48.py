gab  = [1,2,3,4,5,6]
nome = [1,2,3,4]
nota = [1,2,3,4]
ques = [1,2,3,4,5,6]
tot  = 0
def cadastroGabarito():
    print("Cadastro de gabarito")
    for i in range(1,6):
        gab[i] = input("Questao {}: " .format(i))

def cadastroProva():
    notafinal = 0
    print("Respostas dadas")
    for i in range(1,6):
        ques[i] = input("Questao {}: " .format(i))
        if ques[i] == gab[i]:
            notafinal = notafinal + 2
    return notafinal

cadastroGabarito()

for i in range(1,4):
    print("--------------------------")
    print("Aluno ", i)
    print("--------------------------")
    nome[i] = input("Nome: ")
    nota[i] = cadastroProva()
    
print("Notas finais")
for i in range(1,4):
    print(nome[i],   nota[i])
    tot = tot + nota[i]
mt = tot/3
print("Media da turma:  ", mt)
