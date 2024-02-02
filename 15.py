"""Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
salário bruto.
quanto pagou ao INSS.
quanto pagou ao sindicato.
o salário líquido.
calcule os descontos e o salário líquido, conforme a tabela abaixo:
+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$
"""

rcbhr = float(input("Quanto voce ganha por hora? "))
hrpms = int(input("Quantas horas voce trabalha por mes?"))
ir = (rcbhr*hrpms)*0.11
inss = (rcbhr*hrpms)*0.08
sl= (rcbhr*hrpms)-ir - inss - ((rcbhr*hrpms)*0.05)
print("O seu salario mensal  bruto foi calculado em ",rcbhr*hrpms,
      "\nVoce pagou ",inss," Reais ao Inss.",
      "\nVoce pagou ",(rcbhr*hrpms)*0.05," Reais ao sindicato"
      "\nSeu salario mensal liquido foi de R$ ",sl
      )
print("\nA representaçao dos calculos do salario liquido é:",
      "\nSalario Bruto:  ",rcbhr*hrpms,
      "\n           IR - ",ir,
      "\n         Inss - ",inss,
      "\n     Sindicato- ",(rcbhr*hrpms)*0.05,
      "\nSalario Liquido=",sl
      )