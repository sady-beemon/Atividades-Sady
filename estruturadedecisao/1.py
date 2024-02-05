"Faça um Programa que peça dois números e imprima o maior deles.Faça um Programa que peça dois números e imprima o maior deles."

number1 = int(input("Digite o primeiro numero: "))
number2 = int(input("Digite o segundo numero: "))

if number1 > number2:
    print("O primeiro numero é maior.")
elif number2 > number1:
    print("O segundo numero é maior.")
else:
    print("Os numeros sao iguais.")