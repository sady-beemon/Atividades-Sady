"Reverso do número. Faça uma função que retorne o reverso de um número inteiro informado. Por exemplo: 127 -> 721."

def main():

    n = int(input("Digite um numero inteiro: "))
    n = funcao(n)
    print("A quantidade de digitos deste numero é de: ",n)
()
def funcao(n):

    rever = []
    l = list(str(n))
    for i in range(len(l)):
        rever.append(l[((len(l))-1)-i])

    x =''.join(rever)
    return x
()

if __name__ == "__main__":
    main()