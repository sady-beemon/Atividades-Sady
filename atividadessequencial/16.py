"""Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. 
Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total."""

import math
l=0
m2 = int(input("Insira a area em metros quadrados a ser pintada:"))

while True:
    if m2 >= 3:
        l+=1
        m2= m2-3
    elif m2<3 and m2>0:
        break
    elif m2<=0:
        break

lts = l/18
lts = math.ceil(lts)
print("A area pintada precisou de: ", l," litros de tinta. ",
      "\nTotalizando ",lts," latas de tinta de 18 litros.",
      "\nCustando um total de ",lts*80," Reais a R$ 80,00 por lata.")