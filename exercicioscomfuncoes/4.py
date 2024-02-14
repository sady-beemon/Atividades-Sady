"""Faça um programa, com uma função que necessite de um argumento. A função retorna o valor de caractere ‘P’, se seu argumento for positivo, e ‘N’, se seu argumento for zero ou negativo."""

def main():

    n = int(input("Digite um numero inteiro: "))
    l = funcao(n)
    print(l)

()
def funcao(n):
    if n%2 == 0:
        return 'N'
    else:
        return 'P'
()

if __name__ == "__main__":
    main()