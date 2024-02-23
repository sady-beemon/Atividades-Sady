"""Classe carro: Implemente uma classe chamada Carro com as seguintes propriedades:

Um veículo tem um certo consumo de combustível (medidos em km / litro) e uma certa quantidade de combustível no tanque.
O consumo é especificado no construtor e o nível de combustível inicial é 0.
Forneça um método andar( ) que simule o ato de dirigir o veículo por uma certa distância, reduzindo o nível de combustível no tanque de gasolina.
Forneça um método obterGasolina( ), que retorna o nível atual de combustível.
Forneça um método adicionarGasolina( ), para abastecer o tanque. Exemplo de uso:
meuFusca = Carro(15);           # 15 quilômetros por litro de combustível. 
meuFusca.adicionarGasolina(20); # abastece com 20 litros de combustível. 
meuFusca.andar(100);            # anda 100 quilômetros.
meuFusca.obterGasolina()        # Imprime o combustível que resta no tanque."""

class carro:
    def __init__(atributos, andar, gas):
        atributos.km = andar
        atributos.gs = gas
    def metodos(atributos):
        choic = int(input("Escolha uma opçao:\n1 - Km/litro\n2 - adicionar gasolina\n3 - andar\n4 - obter gasolina\n"))
        if choic == 1:
            km = int(input("Digite a quantidade de KM por litro de gasolina: "))
            atributos.km = km
        elif choic == 2:
            gas = int(input("Digite a quantidade de litros que quer abastecer: "))
            atributos.gs += gas
        elif choic == 3:
            andar = int(input("Digite a quantidade de km que quer andar: "))
            gasto = andar/atributos.km
            atributos.gs = atributos.gs - gasto
        elif choic == 4:
            print(atributos.gs)

car = carro(0,0)
while True:
    carro.metodos(car)
    cont = input("Deseja continuar?\n'sim'  'nao' : ")
    if cont == 'nao':
        break