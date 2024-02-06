"Altere o programa anterior para que ele aceite apenas números entre 0 e 1000."

import math

n = []
q = int(input("digite a quantidade de numeros: "))

for i in range(q):
    n1 = float(input("Digite um numero entre 0 e 1000:"))
    if n1 > 1000 or n1 < 0:
        print("Valor invalido, tente novamente")
    else:
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