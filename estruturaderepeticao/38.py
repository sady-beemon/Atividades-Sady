"""Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que:
Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro do percentual do ano anterior. Faça um programa que determine o salário atual desse funcionário. Após concluir isto, altere o programa permitindo que o usuário digite o salário inicial do funcionário.
"""

sal = float(input("Digite seu salario anual: "))
ano =  int(input("Digite o ano que foi contratado: "))
aum = 0.015
while ano != 2024:
    sal = sal + (sal*aum)
    ano +=1
    print("O salario do ano: ",ano," foi de R$ ",round(sal,1)," com uma taxa de aumento anual de: ",round((aum*100),1),"%.")
    aum *= 2