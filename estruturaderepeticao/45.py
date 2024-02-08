"""Desenvolver um programa para verificar a nota do aluno em uma prova com 10 questões, o programa deve perguntar ao aluno a resposta de cada questão e ao final comparar com o gabarito da prova e assim calcular o total de acertos e a nota (atribuir 1 ponto por resposta certa). Após cada aluno utilizar o sistema deve ser feita uma pergunta se outro aluno vai utilizar o sistema. Após todos os alunos terem respondido informar:
Maior e Menor Acerto;
Total de Alunos que utilizaram o sistema;
A Média das Notas da Turma.
Gabarito da Prova:

01 - A
02 - B
03 - C
04 - D
05 - E
06 - E
07 - D
08 - C
09 - B
10 - A"""

g = []
notas = []
mrnota = -1000
mnnota = 1000
a = 0
media = 0

while True:
    ga = (input("Digite a resposta de tantas perguntas que quiser no gabarito(Em Maisculo): \nA - B - C - D - E\nDigite 'quit' quando quiser parar: "))
    if ga == quit:
        break
    g.append(ga)
    

while True:
    p = 0
    for i in range(len(g)):
        print("Selecione sua resposta para questao ",i,
            ":\nA - B - C - D - E")
        res = str(input())
        if g[i] == res:
            p += 1
    notas.append(p)
    if notas[a] >= mrnota:
        mrnota = notas[a]
    if notas[a] <= mnnota:
        mnnota = notas[a]
    cont = int(input("Deseja utilizar o sistema novamente?\nSim - 1   /   Nao - 2  "))
    a += 1
    if cont ==1:
        break

for i in range(len(notas)):
    media += notas[i]
media = media/len(notas)

print("Este foram os resultados da turma:\nMaior e Menor Acerto: ",mrnota," , ",mnnota,
      "\nTotal de Alunos que utilizaram o sistema: ",a,
      "\nA Média das Notas da Turma: ",media)