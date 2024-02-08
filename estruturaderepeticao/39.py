"Faça um programa que leia dez conjuntos de dois valores, o primeiro representando o número do aluno e o segundo representando a sua altura em centímetros. Encontre o aluno mais alto e o mais baixo. Mostre o número do aluno mais alto e o número do aluno mais baixo, junto com suas alturas."

cd = []
alt = []
maior = -1000
menor = 1000

for i in range(10):
    cda = int(input("Digite o codigo do aluno: "))
    alta = float(input("Digite a altura do aluno(em metros): "))
    if alta >= maior:
        maior = alta
        cd1= i
    if alta <= menor:
        menor = alta
        cd2 = i
    cd.append(cda)
    alt.append(alta)

print("\nA lista de alunos ficou a seguinte:\n")
for i in range(len(cd)):
    print(i+1," = O aluno de codigo : ",cd[i]," possue ", alt[i]," metros de altura.")

print("O maior aluno foi o de codigo: ",cd[cd1]," com ",alt[cd1]," metros de altura.")
print("O menor aluno foi o de codigo: ",cd[cd2]," com ",alt[cd2]," metros de altura.")