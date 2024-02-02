"Faça um Programa que peça as 4 notas bimestrais e mostre a média."

nota = 0
for i in range(4):
    number = int(input("Digite a nota do Bimestre:"))
    nota += number
print("A media das notas foi de: ", nota/4)