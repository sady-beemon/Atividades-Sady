"""Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
o produto do dobro do primeiro com metade do segundo .
a soma do triplo do primeiro com o terceiro.
o terceiro elevado ao cubo."""

number1 =int(input("Digite o primeiro numero inteiro: "))
number2 =int(input("Digite o segundo numero inteiro: "))
number3 =float(input("Digite o terceiro numero real"))

print("O dobro do primeiro com a metade do segundo: ",(number1*2)*(number2/2))
print("A soma do triplo do primeiro com o terceiro: ",(number1*3)+number3)
print("O terceiro elevado ao cubo: ",number3**3)