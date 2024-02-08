"""Faça um programa que mostre os n termos da Série a seguir:
  S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m. 
Imprima no final a soma da série."""

"Algumas atividades estao repitidas mesmo: https://wiki.python.org.br/EstruturaDeRepeticao"

n = int(input("Digite n termos da serie: "))

soma = 0
i2 = 1

for i in range(n): 

    resul = (i+1)/i2
    print((i+1)," / ",i2," = ",round(resul,3))
    i2 += 2
    soma += resul

print("Soma das serie de ",n," termos foi de: ",round(soma,1))