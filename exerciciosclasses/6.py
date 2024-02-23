"""Classe TV: Faça um programa que simule um televisor criando-o como um objeto. O usuário deve ser capaz de informar o número do canal e aumentar ou diminuir o volume. Certifique-se de que o número do canal e o nível do volume permanecem dentro de faixas válidas."""

class TV:
    def __init__(atributos, canal,vol):
        atributos.cn = canal
        atributos.vl = vol

    def metodos(atributos):
        choic = int(input("Selecione a opcao desejada:\n1 - Aumentar volume\n2 - Abaixar volume\n3 - Alterar o canal de TV\n"))
        if choic == 1:
            qnt = int(input("Digite a quantidade: "))
            atributos.vl += qnt
        elif choic == 2:
            qnt = int(input("Digite a quantidade: "))
            atributos.vl = atributos.vl - qnt
        elif choic == 3:
            canal = int(input("Digite o numero do canal de TV: "))
            atributos.cn = canal
        else:
            print('A TV foi inalterada')
        if atributos.vl > 100 or atributos.vl < 0:
            print("Volume invalido, colocado em 50.")
            atributos.vl = 50
        elif atributos.cn > 100 or atributos.cn < 0:
            print("Canal invalido, colocado em 50")
            atributos.cn = 50
        print(f"A TV esta atualmente no canal {atributos.cn} no volume {atributos.vl} ")

canal = int(input("Digite o numero do canal de TV: "))
vol = int(input("Digite o volume da TV: "))
cnl = TV(canal,vol)

while True:
    TV.metodos(cnl)
    cont = input("Deseja continuar?\n'sim'  'nao' : ")
    if cont == 'nao':
        break