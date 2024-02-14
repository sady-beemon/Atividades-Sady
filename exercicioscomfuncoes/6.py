"""Faça um programa que converta da notação de 24 horas para a notação de 12 horas. Por exemplo, o programa deve converter 14:25 em 2:25 P.M. A entrada é dada em dois inteiros. Deve haver pelo menos duas funções: uma para fazer a conversão e uma para a saída. Registre a informação A.M./P.M. como um valor ‘A’ para A.M. e ‘P’ para P.M. Assim, a função para efetuar as conversões terá um parâmetro formal para registrar se é A.M. ou P.M. Inclua um loop que permita que o usuário repita esse cálculo para novos valores de entrada todas as vezes que desejar."""

def main():

    while True:
        hrs = int(input("Digite as horas: "))
        min = int(input("Digite os minutos: "))
        p = conversão(hrs,min)
        print(p)
        saida()

()
def conversão(hrs,min):
    min = str(min)
    if hrs > 12:
        hrs = str(hrs -12)
        p = hrs + ":" + min + " P.M"
        return p
    elif hrs >= 0 and hrs <= 12:
        hrs = str(hrs)
        a = ''.join([hrs,':',min,' A.M'])
        return a

()
def saida():
    sair = input("Voce deseja repetir o programa?\nsim - nao: ")
    if sair == 'nao':
        return quit()

if __name__ == "__main__":
    main()