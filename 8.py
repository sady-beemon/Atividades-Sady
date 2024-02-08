"Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor. Imprima a idade e a altura na ordem inversa a ordem lida."

i = []
a = []

for n in range(5):
    v = int(input("Digite a idade de uma das cinco pessoas: "))
    i.append(v)
    v2 = float(input("Digite a altura de uma das cinco pessoas: "))
    a.append(v2)

i.reverse()
a.reverse()
print("Idade: ",i,
      "\nAltura: ",a)