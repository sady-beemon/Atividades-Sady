"""Classe Ponto e Retangulo: Faça um programa completo utilizando funções e classes que:

Possua uma classe chamada Ponto, com os atributos x e y.
Possua uma classe chamada Retangulo, com os atributos largura e altura.
Possua uma função para imprimir os valores da classe Ponto
Possua uma função para encontrar o centro de um Retângulo.
Você deve criar alguns objetos da classe Retangulo.
Cada objeto deve ter um vértice de partida, por exemplo, o vértice inferior esquerdo do retângulo, que deve ser um objeto da classe Ponto.
A função para encontrar o centro do retângulo deve retornar o valor para um objeto do tipo ponto que indique os valores de x e y para o centro do objeto.
O valor do centro do objeto deve ser mostrado na tela
Crie um menu para alterar os valores do retângulo e imprimir o centro deste retângulo."""

class ponto:
    def __init__(pont,y,x):
        pont.x = x
        pont.y = y
        ponto.centro(pont)
    def centro(pont):
        centro = (f'Ponto central = LAR: {pont.x / 2} x ALT: {pont.y/2} ')
        print(centro) 
class retangulo:
    def __init__(atributos, altura, base):
        atributos.al = altura
        atributos.bs = base
    def metodos(atributos):
        choic = int(input("Escolha oque deseja fazer:\n1 - Mudar dimensoes do retangulo.\n2 - Imprimir ponto central:\n"))
        if choic == 1:
            altura = int(input("Digite a altura do retangulo: "))
            base = int(input("Digite a largura do retangulo: "))
            atributos.al = altura
            atributos.bs = base
        elif choic == 2:
            ponto(atributos.al,atributos.bs)
        else:
            print('O tamanho do retangulo continua sendo o mesmo.')
        
        print(f"\nO tamanho de cada dimensao do retangulo atualmente é: {atributos.al} de altura, e {atributos.bs} de largura.\n")

alt = int(input("Digite a altura do retangulo: "))
base = int(input("Digite a largura do retangulo: "))
tri = retangulo(alt,base)
while True:
    retangulo.metodos(tri)
    cont = input("Deseja continuar?\n'sim'  'nao' : ")
    if cont == 'nao':
        break