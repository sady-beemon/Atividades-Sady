"Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles."

number1 =int(input("Digite o primeiro numero: "))
number2 =int(input("Digite o segundo numero: "))

if number1 > number2:
    for i in range(number1-number2):
        print(number1-i)
elif number2 > number1:
    for i in range(number2-number1):
        print(number2-i)
else:
    print("Os numeros sao identicos")