"""Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. O usuário deve informar de qual numero ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:
Tabuada de 5:
5 X 1 = 5
5 X 2 = 10
...
5 X 10 = 50"""

n1 =int(input("Selecione um numero de 1 a 10 para tabuada: "))
if  n1 > 10 or n1 < 1:
    print("Valor invalido.")
else:
    print("A tabuada do numero ecolhido é: ")
    for i in range(1,11):
        print(n1," X ",i," = ",n1 * i)