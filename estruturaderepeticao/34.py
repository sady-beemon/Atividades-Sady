"Os números primos possuem várias aplicações dentro da Computação, por exemplo na Criptografia. Um número primo é aquele que é divisível apenas por um e por ele mesmo. Faça um programa que peça um número inteiro e determine se ele é ou não um número primo."

n = int(input("Digite um numero inteiro positivo: "))
cont = 0
divsisores = []
for i in range(n):
    if n%(i+1)==0:
        cont += 1
        divsisores.append(i+1)

if cont == 2:
    print(n," é um numero real, sendo dividio somente por: ",divsisores)
else:
    print(n," nao é um numero real.")
