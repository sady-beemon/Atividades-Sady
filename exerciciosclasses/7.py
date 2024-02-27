"""Classe Bichinho Virtual:Crie uma classe que modele um Tamagushi (Bichinho Eletrônico):

Atributos: Nome, Fome, Saúde e Idade b. Métodos: Alterar Nome, Fome, Saúde e Idade; Retornar Nome, Fome, Saúde e Idade Obs:
Existe mais uma informação que devemos levar em consideração, o Humor do nosso tamagushi, este humor é uma combinação entre os atributos Fome e Saúde, ou seja,
um campo calculado, então não devemos criar um atributo para armazenar esta informação por que ela pode ser calculada a qualquer momento."""

class bichinho:
    def __init__(self, idade, fome, saude,nome):
        self.saude = saude
        self.fome = fome
        self.idade = idade
        self.nome = nome

    def olhar_bicho(self):
        humor_view = bichinho.calcular_humor(self)
        return f"""
Bichinho de nome: {self.nome}
Nivel de fome: {self.fome}
Idade: {self.idade}
Nivel de saude: {self.saude}
Nivel de humor: {humor_view}
"""
    
    def ler_saude_do_bichinho(self):
        return self.saude

    def atualizar_saude_do_bichinho(self,saude):
        self.saude = saude
        
    def ler_fome_do_bichinho(self):
        return self.fome
    
    def atualizar_fome_do_bichinho(self,fome):
        self.fome = fome
    
    def ler_idade_do_bichinho(self):
        return self.idade
    
    def atualizar_idade_do_bichinho(self,idade):
        self.idade = idade

    def ler_nome_do_bichinho(self):
        return self.nome
    
    def atualizar_nome_do_bichinho(self,nome):
        self.nome = nome

    def calcular_humor(self):
        nivel_de_humor = self.idade + self.saude
        if nivel_de_humor < 50:
            humor = 'malhumor'
        elif nivel_de_humor >= 50 and nivel_de_humor <= 80:
            humor = 'normal'
        else:
            humor = 'Feliz'
        return f"O nivel de humor do bichinho é {humor}"

    def menu(self):
        menu = int(input("Digite a opçao desejada: \n1 - Modificar atributo do bicho.\n2 - Visualizar atributo do bicho\n3 - Ver informaçoes gerais do bichinho\n"))
        if menu == 1:
            bichinho.escolha_atributo_atualizar(self)
        elif menu == 2:
            bichinho.escolha_atributo_visualizar(self)
        elif menu == 3:
            view = bichinho.olhar_bicho(self)
            print(view)
    
    def escolha_atributo_visualizar(self):
        menu = int(input("\nDigite o atrituto desejado para visualizar:\n1 - Nome\n2 - Fome\n3 - Saude\n4 - Idade\n5 - Humor\n"))
        if menu == 1:
            view = bichinho.ler_nome_do_bichinho(self)
            print(view)
        elif menu == 2:
            view = bichinho.ler_fome_do_bichinho(self)
            print(view)
        elif menu == 3:
            view = bichinho.ler_saude_do_bichinho(self)
            print(view)
        elif menu == 4:
            view = bichinho.ler_idade_do_bichinho(self)
            print(view)
        elif menu == 5:
            view = bichinho.calcular_humor(self)
            print(view)
            

    def escolha_atributo_atualizar(self):
        menu = int(input("\nDigite o atributo desejado para atualizar:\n1 - Nome\n2 - Fome\n3 - Saude\n4 - Idade\n "))
        if menu == 1:
            new = str(input("Digite o novo atributo: "))
            bichinho.atualizar_nome_do_bichinho(self,new)
        elif menu == 2:
            new = int(input("Digite o novo atributo: "))
            bichinho.atualizar_fome_do_bichinho(self,new)
        elif menu == 3:
            new = int(input("Digite o novo atributo: "))
            bichinho.atualizar_saude_do_bichinho(self,new)
        elif menu == 4:
            new = int(input("Digite o novo atributo: "))
            bichinho.atualizar_idade_do_bichinho(self,new)
        
        
nome = str(input("Digite o nome do bichinho: "))
idade = int(input("Digite a idade do bichinho: "))
fome = int(input("Digite o nivel de saude do bichinho bichinho(em INT): "))
saude = int(input("Digite o nivel de fome do bichinho(em INT)): "))
p1 = bichinho(idade,fome,saude,nome)
while True:
    bichinho.menu(p1)
    cont = input("Deseja continuar?\n'sim'  'nao' : ")
    if cont == 'nao':
        break