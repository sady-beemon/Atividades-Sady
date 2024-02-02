"""João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho.
 Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso.
 Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar.
 Imprima os dados do programa com as mensagens adequadas."""


pesca = int(input("Digite o peso total dos peixes em KG: "))
if pesca>50:
    quilo=pesca-50
    multa=quilo*4
    print(
        "Voce passou do limite de carga e o excedeu em: ",
        quilo,
        " kg.\nResultando em uma multa de ",
        multa," Reais." 
    )
elif pesca<=50:
    print("Voce esta dentro do limite de carga.")
