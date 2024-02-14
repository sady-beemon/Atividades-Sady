"""Faça um programa para imprimir:
    1
    2   2
    3   3   3
    .....
    n   n   n   n   n   n  ... n
para um n informado pelo usuário. Use uma função que receba um valor n inteiro e imprima até a n-ésima linha."""

def main():

    n = int(input("Digite um numero inteiro: "))

    funcao(n)

()
def funcao(n):
    for i in range(n):
        list = []
        for i2 in range(i+1):
            list.append(i+1)
        print(list,"\n")
()

if __name__ == "__main__":
    main()