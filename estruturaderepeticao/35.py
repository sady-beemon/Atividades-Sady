"Encontrar números primos é uma tarefa difícil. Faça um programa que gera uma lista dos números primos existentes entre 1 e um número inteiro informado pelo usuário."

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

print("A lista de numeros primos entre 1 e o numero digitado é:\n",primos)