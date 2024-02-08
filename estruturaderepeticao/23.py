"""Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário.
O programa deverá mostrar também o número de divisões que ele executou para encontrar os números primos.
Serão avaliados o funcionamento, o estilo e o número de testes (divisões) executados."""

n = int(input("Digite um numero inteiro positivo para servir de ponto final: "))

primos = []
prcont = 0
for i in range(n):
    cont = 0
    for i2 in range(i+1):
        if (i+1)%(i2+1)==0:
            cont += 1

    if cont == 2:
        prcont += 1
        primos.append(i+1)

print(primos)