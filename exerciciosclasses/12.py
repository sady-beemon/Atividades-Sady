"""Classe Conta de Investimento: Faça uma classe contaInvestimento que seja semelhante a classe contaBancaria, com a diferença de que se adicione um atributo taxaJuros. Forneça um construtor que configure tanto o saldo inicial como a taxa de juros. Forneça um método adicioneJuros (sem parâmetro explícito) que adicione juros à conta. Escreva um programa que construa uma poupança com um saldo inicial de R$1000,00 e uma taxa de juros de 10%. Depois aplique o método adicioneJuros() cinco vezes e imprime o saldo resultante."""

class conta:
    def __init__(atributos, saldo, taxa):
        atributos.saldo = saldo
        atributos.juro = taxa

    def escolha_metodo(atributos):
        choic = int(input("Selecione a opcao desejada:\n1 - Modificar Saldo\n2 - Mudar valor de juros \n3 - Adcione juros\n4 - Mostrar informaçoes da conta\n"))
        if choic == 4:
            conta.mostrar_conta(atributos)
        elif choic == 3:
            conta.adcionar_juros(atributos)
        elif choic == 2:
            conta.modificar_valor_juros(atributos)
        elif choic == 1:
            conta.modificar_saldo(atributos)
        else:
            print('A conta foi inalterada')

    def mostrar_conta(atributos):
        print(f"A conta tem um saldo atual de: R$ {atributos.saldo}.  com {atributos.juro}% de juros atuais")

    def modificar_valor_juros(atributos):
            qnt = int(input("Digite o novo valor dos juros: "))
            atributos.juro = qnt

    def adcionar_juros(atributos):
            atributos.saldo = atributos.saldo + (atributos.saldo * (atributos.juro/100))

    def modificar_saldo(atributos):
            qnt = int(input("Digite o valor do novo saldo: "))
            atributos.saldo = qnt


saldo = float(input("Digite o saldo atual da conta: "))
taxa = float(input("Digite o juro inicial da conta: "))
cnt = conta(saldo,taxa)

while True:
    conta.escolha_metodo(cnt)
    cont = input("Deseja continuar?\n'sim'  'nao' : ")
    if cont == 'nao':
        break