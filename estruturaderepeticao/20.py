"Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes e limitando o fatorial a números inteiros positivos e menores que 16."

cont = 'sim'
while cont == 'sim':
    n = int(input("Digite um numero inteiro positivo e menor que 16 a ser fatorado : "))
    if n > 0 and n <16:
        hold = 1
        for i in range(n):
            hold = hold * (i+1)
            print(i," * ",i+1," = ",hold)
    else:
        print("Valor invalido")
    cont = str(input("Calcular outro Fatorial?\nsim -nao\n"))