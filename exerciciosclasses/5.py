"""Classe Conta Corrente: Crie uma classe para implementar uma conta corrente. A classe deve possuir os seguintes atributos: número da conta, nome do correntista e saldo. Os métodos são os seguintes: alterarNome, depósito e saque; No construtor, saldo é opcional, com valor default zero e os demais atributos são obrigatórios."""

class conta:
    def __init__(atributos, nome, saldo, num):
        atributos.sa = saldo
        atributos.nc = num
        atributos.nm = nome
    def metodos(atributos):
        choic = int(input("Selecione a opcao desejada:\n1 - Sacar\n2 - Depositar\n3 - Alterar nome do correntista\n"))
        if choic == 2:
            qnt = int(input("Digite a quantidade: "))
            atributos.sa += qnt
        elif choic == 1:
            qnt = int(input("Digite a quantidade: "))
            atributos.sa = atributos.sa - qnt
        elif choic == 3:
            newname = str(input("Digite o nome do novo correntista: "))
            atributos.nm = newname
        else:
            print('A conta foi inalterada')
        print(f"A conta de numero: {atributos.nc} pertencente a {atributos.nm}, tem um saldo atual de: R$ {atributos.sa}.")

num = int(input("Digite o numero da conta: "))
nome = str(input("Digite o nome do correntista: "))
saldo = float(input("Digite o saldo atual da conta: "))
cnt = conta(nome,saldo,num)

while True:
    conta.metodos(cnt)
    cont = input("Deseja continuar?\n'sim'  'nao' : ")
    if cont == 'nao':
        break