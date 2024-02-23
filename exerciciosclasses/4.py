"""Classe Pessoa: Crie uma classe que modele uma pessoa:

Atributos: nome, idade, peso e altura
Métodos: Envelhercer, engordar, emagrecer, crescer. Obs: Por padrão, a cada ano que nossa pessoa envelhece, sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm."""

class pessoa:
    def __init__(atributos, idade, peso, altura,nome):
        atributos.al = altura
        atributos.ps = peso
        atributos.id = idade
        atributos.nm = nome
    def metodos(atributos):
        mtd = int(input("Selecione um metodo desejado:\n1 - Envelhecer\n2 - engordadar\n3 - emagrecer \n4 - crescer "))
        if mtd == 1:
            if atributos.id < 21:
                atributos.al += 0.5
            atributos.id += 1
        elif mtd == 2:
            qnt = int(input("Digite a quantidade de peso: "))
            atributos.ps += qnt
        elif mtd == 3:
            qnt = int(input("Digite a quantidade de peso: "))
            atributos.ps =  atributos.ps - qnt
        elif mtd == 4:
            qnt = int(input("Digite a quantidade cm a crescer. "))
            atributos.al += qnt
        else:
            print("Elementos nao permanecem os mesmos. ")
        print(f"{atributos.nm} Atualmente tem {atributos.al} cm de altura, pesa {atributos.ps} Kgs e tem {atributos.id} Anos de idade.")

nome = str(input("Digite o nome da pessoa: "))
idade = int(input("Digite a idade da pessoa: "))
peso = int(input("Digite o peso inicial da pessoa(em Kgs): "))
altura = int(input("Digite a altura da pessoa(em Cms): "))
p1 = pessoa(idade,peso,altura,nome)
while True:
    pessoa.metodos(p1)
    cont = input("Deseja continuar?\n'sim'  'nao' : ")
    if cont == 'nao':
        break