i     = 1
maior = 0
print("--------------------------")
print("  Escola Santa Paciencia  ")
print("--------------------------")

tot = int(input("Quantos alunos a turma tem? "))

while i <= tot:
    aluno = input("Nome do aluno: ")
    nota  = int(input("Nota do {}: " .format(aluno)))
    if maior < nota:
        maior  = nota
        maluno = aluno
    i = i + 1




print("O melhor aproveitamento foi de {} com a nota {}" .format(maluno,maior))