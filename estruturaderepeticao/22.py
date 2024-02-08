"""Altere o programa de cálculo dos números primos, informando, caso o número não seja primo, por quais número ele é divisível."""

n = int(input("Digite um numero inteiro positivo: "))
cont = 0
divsisores = []
for i in range(n):
    if n%(i+1)==0:
        cont += 1
        divsisores.append(i+1)

if cont == 2:
    print(n," é um numero primo, sendo dividio somente por: ",divsisores)
else:
    print(n," nao é um numero primo.")
