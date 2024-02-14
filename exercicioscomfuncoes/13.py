"""Desenha moldura. Construa uma função que desenhe um retângulo usando os caracteres ‘+’ , ‘−’ e ‘| ‘. Esta função deve receber dois parâmetros, linhas e colunas, sendo que o valor por omissão é o valor mínimo igual a 1 e o valor máximo é 20. Se valores fora da faixa forem informados, eles devem ser modificados para valores dentro da faixa de forma elegante."""

colu = []
linh = []
def main():

    c = int(input("Digite o numero de colunas: "))
    l = int(input("Digite o numero de linhas: "))        
    check(c,l)

()
def check(c,l):

    if c > 20:
        c = 20
    if l > 20:
        l = 20
    if l < 1:
        l = 1
    if c < 1:
        c = 1
    funcao(c,l)

()
def funcao(c,l):
    for i in range(l):
        lin = str('|')
        linh.append(lin)
    for i in range(c):
        col = str('-')
        colu.append(col)
    x = ''.join(colu)
    for i in range(len(linh)):
        if i == 0 or i == (len(linh)-1):
            print("+",x,"+")
        else:
            print(linh[i]," "*len(x),linh[i])
            
()

if __name__ == "__main__":
    main()