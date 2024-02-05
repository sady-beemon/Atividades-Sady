"Faça um Programa que peça um número e informe se o número é inteiro ou decimal. Dica: utilize uma função de arredondamento."

n1 =  float(input("Digite um numero: "))

if round(n1,0) != n1:
    print("O numero é decimal")
else:
    print("O numero é inteiro.")