"""Utilize uma lista para resolver o problema a seguir. Uma empresa paga seus vendedores com base em comissões. O vendedor recebe $200 por semana mais 9 por cento de suas vendas brutas daquela semana. Por exemplo, um vendedor que teve vendas brutas de $3000 em uma semana recebe $200 mais 9 por cento de $3000, ou seja, um total de $470. Escreva um programa (usando um array de contadores) que determine quantos vendedores receberam salários nos seguintes intervalos de valores:
$200 - $299
$300 - $399
$400 - $499
$500 - $599
$600 - $699
$700 - $799
$800 - $899
$900 - $999
$1000 em diante
Desafio: Crie ma fórmula para chegar na posição da lista a partir do salário, sem fazer vários ifs aninhados.

"""

min = [200,300,400,500,600,700,800,900]
max = [299,399,499,599,699,799,899,999]
sal = []
place = [0,0,0,0,0,0,0,0,0]

while True:
    vend = float(input("Digite o valor das vendas brutas de tantos vendedores desejados: "))
    if vend < 0:
        break
    sal.append(round(200+(vend*0.09),1))
for i in range(len(sal)):
    for i2 in range(len(min)):
        if sal[i] >= min[i2] and sal[i] <= max[i2]:
            place[i2] += 1
    if sal[i] >= 1000:
        place[8] += 1

for i in range(len(min)):
    print("\nSalarios de R$ ",min[i]," - ",max[i]," = ",place[i]," Vendedores.")
print("\nSalarios de Maiores que R$ 1000,00 = ",place[i]," Vendedores.")