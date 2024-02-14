"Faça uma função que informe a quantidade de dígitos de um determinado número inteiro informado."

def main():

    n = int(input("Digite um numero inteiro: "))
    n = funcao(n)
    print("A quantidade de digitos deste numero é de: ",n)
()
def funcao(n):
    n = str(n)
    dgts = len(n)
    return dgts
()

if __name__ == "__main__":
    main()