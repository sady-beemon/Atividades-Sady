"""Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual, e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . )."""

mes = ['Janeiro', 'Fevereiro', 'Marco', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
tmes = []
temp = 0
med = 0

for i in range(12):
    temp = float(input("Digite a temperatura registrada em cada mes do ano: "))
    med += temp
    tmes.append(temp)
med = med/12
print("As temperaturas mensais acima da média anual de ",med," foram os meses de:\n")
for i in range(12):
    if tmes[i] >= med:
        print(i," : ",mes[i]," = ",tmes[i])