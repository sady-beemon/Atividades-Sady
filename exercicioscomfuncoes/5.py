"""Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros formais: taxaImposto, que é a quantia de imposto sobre vendas expressa em porcentagem e custo, que é o custo de um item antes do imposto. A função “altera” o valor de custo para incluir o imposto sobre vendas."""

def main():

    v = int(input("Digite o valor de um item antes do imposto: "))
    tx = int(input("Digite prcentagem de taxas a serem incluidas ao valor base: "))/100
    v = somaImposto(v,tx)
    print("O novo preço do item é de: ",v)

()
def somaImposto(v,tx):
    v = v+(v*tx)
    return v

()

if __name__ == "__main__":
    main()