"Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números."

v = []
s = 0
m = 1

for i in range(5):
    p = int(input("Digite uma sequencia de 5 numeros."))
    s += p
    m *= p
    v.append(p)

print("Os numeros foram: ",v,
      "\nA multiplicaçao dos numeros foi de: ",m,
      "\nA soma dos numeros foi de: ",s)