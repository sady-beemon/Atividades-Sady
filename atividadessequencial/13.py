"""Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
Para homens: (72.7*h) - 58
Para mulheres: (62.1*h) - 44.7"""


altura = float(input("Insira a sua altura: "))
sexo = input("Insira se voce é: \nHomem - 'h' ou Mulher - 'm' ")
if sexo == 'h':
    formula = (72.7*altura) - 58
    print("Com base na sua altura o seu peso ideal seria de: ",formula)
elif sexo == 'm':
    formula = (62.1*altura) - 44.7
    print("Com base na sua altura o seu peso ideal seria de: ",formula)
else:
    print("'Genero nao registrado'")