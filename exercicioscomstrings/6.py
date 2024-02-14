"""Data por extenso. Faça um programa que solicite a data de nascimento (dd/mm/aaaa) do usuário e imprima a data com o nome do mês por extenso.

Data de Nascimento: 29/10/1973
Você nasceu em  29 de Outubro de 1973."""

meses = ['Janeiro','Fevereiro','Abril','Março','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro']

data = str(input("Digite sua data de nascimento neste modelo:\n29/10/1973\n"))
start = 0
mes = ''
dia = ''
ano = ''
for i in range(len(data)):
    if data[i] == '/':
        start += 1
    elif start == 1:
        mes = mes + data[i]
    elif start == 0:
        dia = dia + data[i]
    elif start == 2:
        ano = ano + data[i]
print("Você nasceu em  ",dia," de ",meses[int(mes)-1]," de ",ano,".")
