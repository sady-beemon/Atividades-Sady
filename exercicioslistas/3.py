"Faça um Programa que leia 4 notas, mostre as notas e a média na tela."

v = []
m = 0
for i in range(4):
    p = int(input("Digite uma sequencia de 4 notas."))
    m += p
    v.append(p)

print(v,"\n",m/4)