"Faça um programa que leia 5 números e informe a soma e a média dos números."

n = []

for i in range(5):
    n1 = float(input("Digite um numero:"))
    n.append(n1)

media = 0

for i in n:
    media+=i

print("A soma dos numero é ",media,
      "\nE a media dos numeros é ",media/(len(n)))