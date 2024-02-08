"Faça um programa que calcule o número médio de alunos por turma. Para isto, peça a quantidade de turmas e a quantidade de alunos para cada turma. As turmas não podem ter mais de 40 alunos."

n = int(input("Digite a quantidade turmas: "))
alunos =0

for i in range(n):
    aluno=int(input("Digite a quantidade de alunos em cada turma: "))
    if aluno <= 40 and aluno > 0:
        alunos += aluno
        media = alunos / (i+1)
    else:
        print("As turmas nao podem ter mais de 40 alunos.")

print("A media de alunos é: ",int(media))