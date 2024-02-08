"""Faça um programa que peça um numero inteiro positivo e em seguida mostre este numero invertido.
Exemplo:
  12376489
  => 98467321
"""

numero = int(input("Digite um numero inteiro positivo:"))
rever = []
l = list(str(numero))
for i in range(len(l)):
    rever.append(l[((len(l))-1)-i])

x =''.join(rever)

print("O numero em reverso é: ",x)
