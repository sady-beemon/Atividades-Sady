"""Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
Dicas:
Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
Triângulo Equilátero: três lados iguais;
Triângulo Isósceles: quaisquer dois lados iguais;
Triângulo Escaleno: três lados diferentes;"""

print("Digite 3 lados de um triangulo")
l1 = int(input("1: "))
l2 = int(input("2: "))
l3 = int(input("3: "))

if (l1+l2)>l3 and (l1+l3)>l2 and (l2+l3)>l1:
    print("Isso é um Triangulo!")
    if l1 == l2 and l1 == l3:
        print("Esses lados formam um triangulo Equilatero")
    elif (l1 == l2 and l1 != l3) or (l1 != l2 and l1 == l3):
        print("Esses lados formam um triangulo Isóceles")
    elif l1 != l2 and l1 != l3:
        print("Esses lados formam um triangulo Escaleno")
else:
    print("Isso Nao é um triangulo")

