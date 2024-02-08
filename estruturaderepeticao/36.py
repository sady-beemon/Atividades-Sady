"""Desenvolva um programa que faça a tabuada de um número qualquer inteiro que será digitado pelo usuário, mas a tabuada não deve necessariamente iniciar em 1 e terminar em 10, o valor inicial e final devem ser informados também pelo usuário, conforme exemplo abaixo:
Montar a tabuada de: 5
Começar por: 4
Terminar em: 7

Vou montar a tabuada de 5 começando em 4 e terminando em 7:
5 X 4 = 20
5 X 5 = 25
5 X 6 = 30
5 X 7 = 35
Obs: Você deve verificar se o usuário não digitou o final menor que o inicial."""

n1 =int(input("Selecione um numero  para tabuada: "))
c = int(input("Digite um numero onde a tabuada deve começar: "))
f = int(input("Digite um numero ate onde a tabuada deve acabar: "))

if c > f:
    print("Voce digitou o final menor que o inicial")
else:
    print("\nA tabuada do numero ecolhido é: ")
    print(n1," X ",c," = ",n1 * c)
    for i in range(c,f):
        print(n1," X ",i+1," = ",n1 * (i+1))