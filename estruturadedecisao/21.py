"""Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na máquina.
Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1."""

sq = int(input("O valor mínimo é de 10 reais e o máximo de 600 reais.\nDigite a quantia a sacar: "))

cem = 0
cinq = 0
dez = 0
cinc = 0
um = 0
informe = sq

if sq <= 600 and sq >= 10:

    while sq > 0:
        if sq >= 100:
            cem +=1
            sq = sq -100
        elif sq >= 50: 
            cinq += 1
            sq = sq - 50
        elif sq >=10:
            dez += 1
            sq = sq - 10
        elif sq >= 5:
            cinc += 1
            sq = sq -5
        elif sq >= 1:
            sq =  sq - 1
            um += 1

    print(" Para cobrir o saque de R$ ",informe," Foi fornecido: ",
          "\n",cem," Notas de cem.",
        "\n",cinq," Notas de cinquenta.",
        "\n",dez," Notas de dez.",
        "\n",cinc," Notas de cinco.",
        "\n",um," Notas de um.",
        )
else:
    print("Quantia Invalida")