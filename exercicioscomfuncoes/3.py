"""Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos."""

def main():

    n = int(input("Digite o primeiro numero inteiro: "))
    n2 = int(input("Digite o segundo numero inteiro: "))
    n3 = int(input("Digite o terceiro numero inteiro: "))

    funcao(n,n2,n3)

()
def funcao(n,n2,n3):
    soma = n2+n3+n
    print(soma)
()

if __name__ == "__main__":
    main()