"""Classe Bola: Crie uma classe que modele uma bola:

Atributos: Cor, circunferência, material
Métodos: trocaCor e mostraCor"""

class bola:
    def __init__(atributos, cor, circ, mat):
        atributos.c = cor
        atributos.circ = circ
        atributos.m = mat
    def metodos(atributos):
        choic = input("Deseja mudar a cor da bola?\n'sim'   'nao' : ")
        if choic == 'sim':
            ncor = input("Digite a nova cor: ")
            atributos.c = ncor
        else:
            print('A cor continua sendo a mesma.')
        print(f"A cor atual é: {atributos.c}")

corfirst = str(input("Digite a primeira cor."))
bl = bola(corfirst,0,'aleatorio')
while True:
    bola.metodos(bl)
    cont = input("Deseja continuar?\n'sim'  'nao' : ")
    if cont == 'nao':
        break