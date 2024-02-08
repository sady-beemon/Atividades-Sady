"""Faça um programa que receba o valor de uma dívida e mostre uma tabela com os seguintes dados: valor da dívida, valor dos juros, quantidade de parcelas e valor da parcela.
Os juros e a quantidade de parcelas seguem a tabela abaixo:
Quantidade de Parcelas  % de Juros sobre o valor inicial da dívida
1       0
3       10
6       15
9       20
12      25
Exemplo de saída do programa:
Valor da Dívida Valor dos Juros Quantidade de Parcelas  Valor da Parcela
R$ 1.000,00     0               1                       R$  1.000,00
R$ 1.100,00     100             3                       R$    366,00
R$ 1.150,00     150             6                       R$    191,67"""

v1 = int(input("Digite o valor da divida."))
par = -2
j=0

print("Valor da Dívida /// Valor dos Juros /// Quantidade de Parcelas  /// Valor da Parcela")
for i in range(5):
    par += 3
    if par == 3:
        j = 0.1
    elif par == 6:
        j = 0.15
    elif par == 9:
        j = 0.2
    elif par == 12:
        j = 0.25
    print(v1+(v1*j),"               ",v1*j,"            ",par,"                       ",    round(((v1+(v1*j))/par),1 ))
    if par == 1:
        par = 0