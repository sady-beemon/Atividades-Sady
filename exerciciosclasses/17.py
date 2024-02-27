"""Crie uma Fazenda de Bichinhos instanciando vários objetos bichinho e mantendo o controle deles através de uma lista. 
Imite o funcionamento do programa básico, mas ao invés de exigis que o usuário tome conta de um único bichinho, exija que ele tome conta da fazenda inteira.
 Cada opção do menu deveria permitir que o usuário executasse uma ação para todos os bichinhos (alimentar todos os bichinhos, brincar com todos os bichinhos,
   ou ouvir a todos os bichinhos). Para tornar o programa mais interessante, dê para cada bichinho um nivel inicial aleatório de fome e tédio."""

bichinhos = []
import random

class Bichinho:
    def __init__(atributos,nome ,idade, fome, sd, brinc):
        atributos.sd = sd
        atributos.fm = fome
        atributos.id = idade
        atributos.nm = nome
        atributos.br = brinc

    def visualizar(atributos):
        humor = 0
        if atributos.fm >= 60:
            humor += 1
        if atributos.sd >= 60:
            humor += 1
        if atributos.br >= 60:
            humor += 1
        print(f"{atributos.nm} Atualmente tem {atributos.sd} pontos de saude, {atributos.fm} pontos de fome, {atributos.br} de brincadeira, e ele tem {atributos.id} Anos de idade.")
        if humor <= 0:
            print("O bichino atualmente esta muito mal humorado.")
        elif humor <= 2:
            print("O bichino atualmente esta emburrado.")
        elif humor == 3:
            print("O bichino atualmente esta bem humorado.")


    def escolha():
        mtd = int(input("Selecione um metodo desejado para adicionar(ou subtrarir) para todos os bichinhos:\n1 - Envelhecer\n2 - Alimentar\n3 - Cuidar (aumentar saude) \n4 - Brincar:\n5 - Nao fazer Nada "))
        if mtd == 1:
            Bichinho.envelhecer_todos()
        elif mtd == 2:
            Bichinho.alimentar_todos()
        elif mtd == 3:
            Bichinho.cuidar_todos()
        elif mtd == 4:
            Bichinho.brincar_todos()
        else: 
            print("Nada acontece.")

    def envelhecer_todos():
        qnt = int(input("Digite a quantidade de anos que cada bichinho envelheceu: "))
        for i in range(len(bichinhos)):
            bichinhos[i].id+= qnt

    def alimentar_todos():
        qnt = int(input("Digite a quantidade de alimento quer dar a cada bichinho: "))
        for i in range(len(bichinhos)):
            bichinhos[i].fm += qnt

    def brincar_todos():
        qnt = int(input("Digite o tempo que quer brincar com cada bichinho: "))
        for i in range(len(bichinhos)):
            bichinhos[i].br += qnt

    def cuidar_todos():
        qnt = int(input("Digite a quantidade de cuidado dedicado a cada bichinho: "))
        for i in range(len(bichinhos)):
            bichinhos[i].sd += qnt

        
def add():
    nome = str(input("Digite o nome do bichinho:\nOs outros itens serao preenchidos aleatoriamente\n"))
    p1 = Bichinho(nome,idade = random.randint(1,25), fome = random.randint(30,80), sd = random.randint(35,85) ,brinc = random.randint(15,85))
    return p1

def fazenda():
    menu = int(input("Selecione uma opçao:\n1 - Visualizar bichinho\n2 - Adicionar bichinho\n3 - Modificar todos\n4 - Sair do programa\n"))
    if menu == 1:
        print("0 = sair\nSelecione um bichinho: ")
        for i in range(len(bichinhos)):
            print(f"{i+1} : {bichinhos[i].nm}")
        i = int(input("\n"))
        if i == 0:
            False
        else:
            Bichinho.visualizar(bichinhos[i-1])
    elif menu == 2:
        p1 = add()
        bichinhos.append(p1)
    elif menu == 3:
        Bichinho.escolha()
    elif menu == 4:
        cont = input("Deseja continuar?\n'sim'  'nao' : ")
        if cont == 'sim':
            quit()
while True:
    fazenda()