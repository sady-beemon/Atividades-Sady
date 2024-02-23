"""Crie uma "porta escondida" no programa do programa do bichinho virtual que mostre os valores exatos dos atributos do objeto. Consiga isto mostrando o objeto quando uma opção secreta, não listada no menu, for informada na escolha do usuário. Dica: acrescente um método especial str() à classe Bichinho.
"""

class bichinho:
    def __init__(atributos, idade, fome, sd,nome,brinc):
        atributos.sd = sd
        atributos.fm = fome
        atributos.id = idade
        atributos.nm = nome
        atributos.br = brinc
    def metodos(atributos):
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
        elif mtd == 6:
            hidden = str(input("Escreva um atributo adicional ao nome do bichinho: "))
        else:
            print("Elementos nao permanecem os mesmos. ")
        print(f"{atributos.nm + ' ' + hidden} Atualmente tem {atributos.sd} pontos de saude, {atributos.fm} pontos de fome, voce brincou {atributos.br} minutos com ele, e ele tem {atributos.id} Anos de idade. Deixando seu nivel de humor/felicidade em {(atributos.sd*atributos.fm*atributos.br)/10000}%")

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