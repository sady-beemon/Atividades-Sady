"""Crie uma "porta escondida" no programa do programa do bichinho virtual que mostre os valores exatos dos atributos do objeto.
Consiga isto mostrando o objeto quando uma opção secreta, não listada no menu, for informada na escolha do usuário.
 Dica: acrescente um método especial str() à classe Bichinho.
"""

class bichinho:
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


    def escolha(atributos):
        mtd = int(input("Selecione um metodo desejado para adicionar(ou subtrarir) para todos os bichinhos:\n1 - Envelhecer\n2 - Alimentar\n3 - Cuidar (aumentar saude) \n4 - Brincar:\n5 - Nao fazer Nada "))
        if mtd == 1:
            bichinho.envelhecer_todos(atributos)
        elif mtd == 2:
            bichinho.alimentar_todos(atributos)
        elif mtd == 3:
            bichinho.cuidar_todos(atributos)
        elif mtd == 4:
            bichinho.brincar_todos(atributos)
        elif mtd == 5:
            bichinho.visualizar(atributos) 
        else:    
            print("Nada acontece.")

    def envelhecer_todos(atributos):
        qnt = int(input("Digite a quantidade de anos que cada bichinho envelheceu: "))
        atributos.id += qnt

    def alimentar_todos(atributos):
        qnt = int(input("Digite a quantidade de alimento quer dar a cada bichinho: "))
        atributos.fm += qnt

    def brincar_todos(atributos):
        qnt = int(input("Digite o tempo que quer brincar com cada bichinho: "))
        atributos.br += qnt

    def cuidar_todos(atributos):
        qnt = int(input("Digite a quantidade de cuidado dedicado a cada bichinho: "))
        atributos.sd += qnt

nome = str(input("Digite o nome do bichinho: "))
idade = int(input("Digite a idade do bichinho: "))
fome = int(input("Digite o nivel de saude do bichinho bichinho(em INT): "))
sd = int(input("Digite o nivel de fome do bichinho(em INT)): "))
brinc = int(input("Digite quantos minutos voce quer brincar com o bichinho: "))
p1 = bichinho(nome,idade,fome,sd,brinc)
while True:
    bichinho.escolha(p1)
    cont = input("Deseja continuar?\n'sim'  'nao' : ")
    if cont == 'nao':
        break