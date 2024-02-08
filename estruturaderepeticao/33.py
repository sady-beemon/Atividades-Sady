"""O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia as um conjunto indeterminado de temperaturas, e informe ao final a menor e a maior temperaturas informadas, bem como a média das temperaturas."""

temperaturas = int(input("Digite a quantidade temperaturas registradas: "))
tmps =[]
menor = 1000
maior = -1000

for i in range(temperaturas):
    print("Digite o valor de cada temperatura: ")
    tmp=float(input())
    if tmp <= menor:
        menor = tmp
    if tmp >= maior:
        maior = tmp
    tmps.append(tmp)

print("\nTemperaturas registradas:\n")
for i in range(len(tmps)):
    print(i+1," Cº ",round(tmps[i],1))

print("A maior temperatura registrada foi de: ",maior,
      "\nA menor temperatura registrada foi de: ",menor)