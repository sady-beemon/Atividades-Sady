"""Faça um programa que use a função valorPagamento para determinar o valor a ser pago por uma prestação de uma conta. O programa deverá solicitar ao usuário o valor da prestação e o número de dias em atraso e passar estes valores para a função valorPagamento, que calculará o valor a ser pago e devolverá este valor ao programa que a chamou. O programa deverá então exibir o valor a ser pago na tela. Após a execução o programa deverá voltar a pedir outro valor de prestação e assim continuar até que seja informado um valor igual a zero para a prestação. Neste momento o programa deverá ser encerrado, exibindo o relatório do dia, que conterá a quantidade e o valor total de prestações pagas no dia. O cálculo do valor a ser pago é feito da seguinte forma. Para pagamentos sem atraso, cobrar o valor da prestação. Quando houver atraso, cobrar 3% de multa, mais 0,1% de juros por dia de atraso."""

def main():        
    presttl = 0
    vlrttl = 0
    while True:

        prest = float(input("Digite o valor da prestaçao(Para parar digite 0): R$ "))
        if prest == 0:
            print("quantidade total de prestaçoes pagas no dia: ",presttl,
                "\nValor total das prestaçoes pagas no dia: R$ ",vlrttl)
            quit()
        presttl += 1
        limite = int(input("Qual é o limite de dias para pagar a prestaçao: "))
        dias = int(input("Digite a quantidade de dias em atraso: "))
        vlrfinal = valorpagamento(prest,limite,dias)
        print("O valor final desta prestaçao é de: R$",vlrfinal)
        vlrttl += vlrfinal

def valorpagamento(prest,limite,dias):
    if dias > limite:
        prest += (prest*(dias-limite))*0.001 + (prest*0.03)
        return prest
    else:
        return prest    


if __name__ == "__main__":
    main()