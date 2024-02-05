"""Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;"""

a = int(input("Digite o primeiro quociente A:"))
b = int(input("Digite o segundo quociente B:"))
c = int(input("Digite o terçeiro quociente C:"))
delta = ((b**2) - (4 * a * c ))

if delta < 0:
    print("Essa equaçao nao tem raizes")
elif delta == 0:
    print("Essa equaçao tem uma raiz com valor de:")
    r1 = b/(2*a)
    print(r1)
elif delta > 0:
    print("essa equaçao tem duas raizes com valores de:")
    r1 = b/(2*a)
    r2 = -b/(2*a)
    print(r1,"\n",r2)