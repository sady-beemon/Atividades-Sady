"""Classe Bichinho Virtual++: Melhore o programa do bichinho virtual, permitindo que o usuário especifique quanto de comida ele fornece ao bichinho e por quanto tempo ele brinca com o bichinho. Faça com que estes valores afetem quão rapidamente os níveis de fome e tédio caem."""

class bichinho:
    def __init__(atributos, idade, fome, sd,nome,brinc):
        atributos.sd = sd
        atributos.fm = fome
        atributos.id = idade
        atributos.nm = nome
        atributos.br = brinc
    def metodos(atributos):
        humor = 0
        if atributos.fm >= 60:
            humor += 1
        if atributos.sd >= 60:
            humor += 1
        if atributos.br >= 60:
            humor += 1
        print(f"{atributos.nm} Atualmente tem {atributos.sd} pontos de saude, {atributos.fm} pontos de fome, voce brincou {atributos.br} minutos com ele, e ele tem {atributos.id} Anos de idade.")
        if humor <= 1:
            print("O bichino atualmente esta muito mal humorado.")
        elif humor == 2:
            print("O bichino atualmente esta emburrado.")
        elif humor == 3: 
            print("O bichino atualmente esta bem humorado.")
        mtd = int(input("Selecione um metodo desejado para alterar:\n1 - Idade\n2 - Fome\n3 - Saude \n4 - Nome\n5 - Brincar "))
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
            nome = str(input("Digite o novo nome do bichinho:  "))
            atributos.nm = nome
        elif mtd == 5:
            brinc = int(input("Digite quantos minutos voce quer brincar com o macaco: "))
            atributos.br += brinc
            atributos.fm = atributos.fm - (brinc/2)
            if atributos.br > 100:
                print("O bichinho esta cansado de tanto brincar:")
                atributos.br = 100
        else:
            print("Elementos nao permanecem os mesmos. ")

nome = str(input("Digite o nome do bichinho: "))
idade = int(input("Digite a idade do bichinho: "))
fome = int(input("Digite o nivel de saude do bichinho bichinho(em INT): "))
sd = int(input("Digite o nivel de fome do bichinho(em INT)): "))
brinc = int(input("Digite quantos minutos voce quer brincar com o bichinho: "))
p1 = bichinho(idade,fome,sd,nome,brinc)
while True:
    bichinho.metodos(p1)
    cont = input("Deseja continuar?\n'sim'  'nao' : ")
    if cont == 'nao':
        break