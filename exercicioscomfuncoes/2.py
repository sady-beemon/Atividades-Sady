"""Faça um programa para imprimir:
    1
    1   2
    1   2   3
    .....
    1   2   3   ...  n"""

def main():

    n = int(input("Digite um numero inteiro: "))

    funcao(n)

()
def funcao(n):
    for i in range(n):
        list = []
        for i in range(i+1):
            list.append(i+1)
        print(list,"\n")
()

if __name__ == "__main__":
    main()