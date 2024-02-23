"""Classe Retangulo: Crie uma classe que modele um retangulo:

Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;
Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as medidades de um local. Depois, deve criar um objeto com as medidas e calcular a quantidade de pisos e de rodapés necessárias para o local.
"""

class triangulo:
    def __init__(atributos, altura, base):
        atributos.al = altura
        atributos.bs = base
    def metodos(atributos):
        choic = input("Deseja mudar o tamanho dos lado?\n'sim'   'nao' : ")
        if choic == 'sim':
            altura = int(input("Digite a altura do triangulo: "))
            base = int(input("Digite a base do triangulo: "))
            atributos.al = altura
            atributos.bs = base
        else:
            print('O tamanho do triangulo continua sendo o mesmo.')
        print(f"O tamanho de cada dimensao atualmente é: {atributos.al} de altura, e, {atributos.bs} de base.\nO tamanho da area é {(atributos.al * atributos.bs)/2 }")

alt = int(input("Digite a altura do triangulo: "))
base = int(input("Digite a base do triangulo: "))
tri = triangulo(alt,base)
while True:
    triangulo.metodos(tri)
    cont = input("Deseja continuar?\n'sim'  'nao' : ")
    if cont == 'nao':
        break