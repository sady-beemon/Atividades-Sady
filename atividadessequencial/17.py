"""
Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.
"""
import math
l=0
ltsn=0
glsn=0
m2 = int(input("Insira a area em metros quadrados a ser pintada:"))

while True:
    if m2 >= 6:
        l+=1
        m2= m2-6
    elif m2<6 and m2>0:
        break
        l+=1
    elif m2<=0:
        break
ls=l

lts = l/18
gls = l/3.6
lts = math.ceil(lts)
gls = math.ceil(gls)

while True:
    if l>10.8:
        ltsn+=1
        l=l-18
    elif l<=10.8 and l>0:
        glsn+=1
        l=l-3.6
    else:
        break


print("A area pintada precisou de: ", ls," litros de tinta. ",
      "\nTotalizando ",lts," latas de tinta de 18 litros.",
      "\nOu",gls," galoes de tinta de 3.6 litros",
      "\nCustando um total de ",lts*80," Reais a R$ 80,00 por lata. Comprando somente latas.",
      "\nOu, custando um total de ",gls*25," Reais a R$ 25,00 por galao. Comprando somente galoes.",
      "\n\nE para a compra mais eficiente misturando galoes e latas.",
      "\nO custo foi de ",(glsn*25)+(ltsn*80)," Reais, comprando ",glsn," galoes de tinta, e ",ltsn," latas de tinta."
      
      )