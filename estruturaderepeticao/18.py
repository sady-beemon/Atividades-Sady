"Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores."
import math

n = []
q = int(input("digite a quantidade de numeros: "))

for i in range(q):
    n1 = float(input("Digite um numero:"))
    n.append(n1)

high = -math.inf
low = math.inf
soma = 0

for i in n:
    if i >=  high:
        high = i
    if i <= low:
        low = i
    soma += i

print("O maior numero foi ",high,
      "\nO menor numero foi ",low,
      "\nA soma de todos os numeros foi ",soma)