"""Classe Bichinho Virtual:Crie uma classe que modele um Tamagushi (Bichinho Eletrônico):

Atributos: Nome, Fome, Saúde e Idade b. Métodos: Alterar Nome, Fome, Saúde e Idade; Retornar Nome, Fome, Saúde e Idade Obs: Existe mais uma informação que devemos levar em consideração, o Humor do nosso tamagushi, este humor é uma combinação entre os atributos Fome e Saúde, ou seja, um campo calculado, então não devemos criar um atributo para armazenar esta informação por que ela pode ser calculada a qualquer momento."""

class bichinho:
    def __init__(atributos, idade, fome, sd,nome):
        atributos.sd = sd
        atributos.fm = fome
        atributos.id = idade
        atributos.nm = nome
    def metodos(atributos):
        mtd = int(input("Selecione um metodo desejado para alterar:\n1 - Idade\n2 - Fome\n3 - Saude \n4 - Nome "))
        if mtd == 1:
            ida = int(input("Digite a idade nova do bichinho: "))
            atributos.id = ida
        elif mtd == 2:
            qnt = int(input("Digite o novo nivel de fome do bichinho: "))
            atributos.fm = qnt
        elif mtd == 3:
            qnt = int(input("Digite o novo nivel de saude do bichinho: "))
            atributos.sd =  qnt
        elif mtd == 4:
            nome = str(input("Digite o novo nome do bichinho. "))
            atributos.nm = nome
        else:
            print("Elementos nao permanecem os mesmos. ")
        print(f"{atributos.nm} Atualmente tem {atributos.sd} pontos de saude, {atributos.fm} pontos de fome e {atributos.id} Anos de idade. Deixando seu nivel de humor/felicidade em {(atributos.sd*atributos.fm)/100}")

nome = str(input("Digite o nome do bichinho: "))
idade = int(input("Digite a idade do bichinho: "))
fome = int(input("Digite o nivel de saude do bichinho bichinho(em INT): "))
sd = int(input("Digite o nivel de fome do bichinho(em INT)): "))
p1 = bichinho(idade,fome,sd,nome)
while True:
    bichinho.metodos(p1)
    cont = input("Deseja continuar?\n'sim'  'nao' : ")
    if cont == 'nao':
        break