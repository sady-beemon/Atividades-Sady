"""Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120. A saída deve ser conforme o exemplo abaixo:
Fatorial de: 5
5! =  5 . 4 . 3 . 2 . 1 = 120"""

s= []
n = int(input("Digite o numero a ser fatorado: "))
hold = 1
for i in range(n):
    hold = hold * (i+1)
    s.append(i+1)
    print(n," = ",s," = ",hold)