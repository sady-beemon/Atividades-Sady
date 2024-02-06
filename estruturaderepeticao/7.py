"Faça um programa que leia 5 números e informe o maior número."

n = []

for i in range(5):
    n1 = float(input("Digite um numero:"))
    n.append(n1)

high = -1000

for i in n:
    if i >=  high:
        high = i

print("O maior numero foi ",high)