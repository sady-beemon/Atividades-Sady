"Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos quadrados dos elementos do vetor."

v = []
s = 0
for i in range(10):
    p = int(input("Digite uma sequencia de 10 numeros."))
    s+= p**2
    v.append(p)

print("A soma dos quadrados dos elementos foi de: ", s)