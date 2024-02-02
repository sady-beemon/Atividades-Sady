"""Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
C = 5 * ((F-32) / 9)."""

faren=float(input("Digite uma temperatura em Fahrenheit: "))
c = 5*((faren-32) / 9)
print("Essa mesma temperatura em graus Celsius é de: ", c ," Graus.")