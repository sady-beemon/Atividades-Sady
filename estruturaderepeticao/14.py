"Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares."

n = []
par = 0
impar = 0

for i in range(10):
    n1 = float(input("Digite um numero:"))
    n.append(n1)
    if n1%2==0:
        par += 1
    else:
        impar += 1

print("A quantidade de numeros pares é ",par,
      "\nA quantidade de numeros impares é ",impar)