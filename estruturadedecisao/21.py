"""Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas.
As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais.
O valor mínimo é de 10 reais e o máximo de 600 reais.
O programa não deve se preocupar com a quantidade de notas existentes na máquina.
Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1."""

saque = int(input("O valor mínimo é de 10 reais e o máximo de 600 reais.\nDigite a quantia a sacar: "))

qtd_notas_cem = 0
qtd_notas_cinquenta = 0
qtd_notas_dez = 0
qtd_notas_cinco = 0
qtd_notas_um = 0
informe = saque

if saque <= 600 and saque >= 10:

    while saque:
        if saque >= 100:
            qtd_notas_cem +=1
            saque -= 100
        elif saque >= 50: 
            qtd_notas_cinquenta += 1
            saque -=  50
        elif saque >=10:
            qtd_notas_dez += 1
            saque -=  10
        elif saque >= 5:
            qtd_notas_cinco += 1
            saque -= 5
        elif saque >= 1:
            saque =  saque - 1
            qtd_notas_um += 1

    print(" Para cobrir o saque de R$ ",informe," Foi fornecido: ",
          "\n",qtd_notas_cem," Notas de cem.",
        "\n",qtd_notas_cinquenta," Notas de cinquenta.",
        "\n",qtd_notas_dez," Notas de dez.",
        "\n",qtd_notas_cinco," Notas de cinco.",
        "\n",qtd_notas_um," Notas de um.",
        )
else:
    print("Quantia Invalida")