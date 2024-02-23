"""Classe Bomba de Combustível: Faça um programa completo utilizando classes e métodos que:

Possua uma classe chamada bombaCombustível, com no mínimo esses atributos:
tipoCombustivel.
valorLitro
quantidadeCombustivel
Possua no mínimo esses métodos:
abastecerPorValor( ) – método onde é informado o valor a ser abastecido e mostra a quantidade de litros que foi colocada no veículo
abastecerPorLitro( ) – método onde é informado a quantidade em litros de combustível e mostra o valor a ser pago pelo cliente.
alterarValor( ) – altera o valor do litro do combustível.
alterarCombustivel( ) – altera o tipo do combustível.
alterarQuantidadeCombustivel( ) – altera a quantidade de combustível restante na bomba.
OBS: Sempre que acontecer um abastecimento é necessário atualizar a quantidade de combustível total na bomba."""

class bomba:
    def __init__(atributos, vlr,tipo,quanti):
        atributos.qnt = quanti
        atributos.vlr = vlr
        atributos.tip = tipo
    def metodos(atributos):
        choic = int(input("Digite a opçao desejada: \n1- Abastecer Por Valor\n2 - Abastecer Por Litro\n3 - Visualizar informaçoes do tipo de combustivel na bomba \n4 - Alterar valor do combustivel\n5 - Alterar quantidade de combustivel restante: \n"))
        if choic == 1:
            qntdin = int(input("Digite a quantidade de dinheiro: R$ "))
            qntgas = (qntdin/atributos.vlr)
            print(f"Com esse dinheiro foi abestecido2 {qntgas} litros de gasolina.")
            atributos.qnt = atributos.qnt - qntgas
        elif choic == 2:
            qntgas = int(input("Digite a quantidade de litros: "))
            qntdin = qntgas*atributos.vlr
            print(f"Por {qntgas} litros de gasolina o valor pago foi de: R$ {qntdin}.")
            atributos.qnt = atributos.qnt - qntgas
        elif choic == 3:
            print(f"O tipo de gasolina {atributos.tip} custa {atributos.vlr} reais por litro e tem {atributos.qnt} litros restantes na bomba. ")
        elif choic == 4:
            din = float(input("Digite o novo preço por litro deste tipo de combustivel: "))
            atributos.vlr = din
        elif choic == 5:
            qnt = float(input("Digite a nova quantidade deste combustivel na bomba: "))
            atributos.qnt = qnt
        

gas = str(input("Digite um dos tipos de combustivel dessa bomba: "))
vlr = float(input("Digite o valor por litro deste mesmo tipo de combustivel: "))
qnt = float(input("Digite a quantidade deste combustivel na bomba."))
bombagas = bomba(vlr,gas,qnt)

while True:
    bomba.metodos(bombagas)
    cont = input("Deseja continuar?\n'sim'  'nao' : ")
    if cont == 'nao':
        break