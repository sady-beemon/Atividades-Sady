"Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo."

valor = float(input("Digite um numero: "))

if valor>0:
    print("O numero é positivo.")
elif valor<0:
    print("O numero é negativo.")
else:
    print("Zero.")