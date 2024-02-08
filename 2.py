"Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa."

v = []

for i in range(10):
    p = int(input("Digite uma sequencia de 10 numeros."))
    v.append(p)

v.reverse()
print(v)