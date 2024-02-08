"Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0."

med = []
maior = 0

for i in range(10):
    m = 0
    print("Digite as 4 notas de um aluno: ")
    for i2 in range(4):
        n = float(input("= "))
        m += n
    m = m/4
    if m >= 7:
        maior += 1
    med.append(m)

print("O vetor da media dos alunos foi: ",med,
      "\nA quantidade de alunos com media > 7 foi de: ", maior)