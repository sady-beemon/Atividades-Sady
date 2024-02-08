"""Sendo H= 1 + 1/2 + 1/3 + 1/4 + ... + 1/N, Faça um programa que calcule o valor de H com N termos."""

h = int(input("Digite o valor de H"))
n = int(input("Digite a quantidade de termos: "))
r = []

for i in range(n):
    c = h/(i+1)
    print(i+1,"º termo: ",h," / ",i+1," = ",round(c,5))