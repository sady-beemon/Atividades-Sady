"""Classe Quadrado: Crie uma classe que modele um quadrado:

Atributos: Tamanho do lado
Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;"""

class quadrado:
    def __init__(atributos, lado):
        atributos.l = lado
    def metodos(atributos):
        choic = input("Deseja mudar o tamanho do lado?\n'sim'   'nao' : ")
        if choic == 'sim':
            nlado = input("Digite o novo tamanho de cada lado: ")
            atributos.l = nlado
        else:
            print('O tamanho do lado continua sendo o mesmo.')
        print(f"O tamanho de cada lado atualmente é: {atributos.l}\nO tamanho da area é {int(atributos.l) ** 2}")

ladofirst = int(input("Digite o primeiro tamanho de cada lado: "))
qdr = quadrado(ladofirst)
qdr.l = ladofirst
while True:
    quadrado.metodos(qdr)
    cont = input("Deseja continuar?\n'sim'  'nao' : ")
    if cont == 'nao':
        break