"""Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. Um número primo é aquele que é divisível somente por ele mesmo e por 1."""

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
