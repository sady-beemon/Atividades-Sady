"""Classe Conta de Investimento: Faça uma classe contaInvestimento que seja semelhante a classe contaBancaria, com a diferença de que se adicione um atributo taxaJuros. Forneça um construtor que configure tanto o saldo inicial como a taxa de juros. Forneça um método adicioneJuros (sem parâmetro explícito) que adicione juros à conta. Escreva um programa que construa uma poupança com um saldo inicial de R$1000,00 e uma taxa de juros de 10%. Depois aplique o método adicioneJuros() cinco vezes e imprime o saldo resultante."""

class conta:
    def __init__(atributos, saldo, taxa):
        atributos.sa = saldo
        atributos.tx = taxa
    def metodos(atributos):
        choic = int(input("Selecione a opcao desejada:\n1 - Modificar Saldo\n2 - Mudar valor de juros \n3 - Adcione juros\n"))
        if choic == 1:
            qnt = int(input("Digite o valor do novo saldo: "))
            atributos.sa = qnt
        elif choic == 2:
            qnt = int(input("Digite a quantidade: "))
            atributos.tx = qnt
        elif choic == 3:
            print(atributos.sa)
            atributos.sa = atributos.sa + (atributos.sa * (atributos.tx/100))
            
        else:
            print('A conta foi inalterada')
        print(f"A conta tem um saldo atual de: R$ {atributos.sa}.  com {atributos.tx/100}% de juros atuais")


saldo = float(input("Digite o saldo atual da conta: "))
taxa = float(input("Digite o juro inicial da conta: "))
cnt = conta(saldo,taxa)

while True:
    conta.metodos(cnt)
    cont = input("Deseja continuar?\n'sim'  'nao' : ")
    if cont == 'nao':
        break