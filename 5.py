"Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores."

par = []
imp = []

for i in range(20):
    p = int(input("Digite uma sequencia de 20 numeros."))
    if p%2==0:
        par.append(p)
    else:
        imp.append(p)

print("Pares: ",par,
      "\nImpares: ",imp)