"""Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto, o mais baixo, a mais gordo e o mais magro, para isto você deve fazer um programa que pergunte a cada um dos clientes da academia seu código, sua altura e seu peso. O final da digitação de dados deve ser dada quando o usuário digitar 0 (zero) no campo código. Ao encerrar o programa também deve ser informados os códigos e valores do clente mais alto, do mais baixo, do mais gordo e do mais magro, além da média das alturas e dos pesos dos clientes"""

import math

alt = []
cli = []
pes = []
maiora = -1000
menora = 1000
maiorp = -1000
menorp = 1000
i=0

while True:

    c = int(input("Digite o codigo do cliente: "))
    if c == 0:
        break
    cli.append(c)
    a = float(input("Digite a altura desse mesmo cliente(em metros): "))
    if a >= maiora:
        maiora = a
        cdmra = i
    if a <= menora:
        menora = a
        cdmna = i
    p = float(input("Digite o peso desse mesmo cliente(em kg): "))
    if p >= maiorp:
        maiorp = p
        cdmrp = i
    if p <= menorp:
        menorp = p
        cdmnp = i
    alt.append(a)
    pes.append(p)
    i+=1

print("\nA lista de clientes montadas foi a seguinte:\n")
for i in range(len(cli)):
    print(i+1," = Codigo: ",cli[i],". Altura : ",alt[i],". Peso : ",pes[i])

print("O cliente mais alto foi o de codigo = ",cli[cdmra]," com ",alt[cdmra]," m de altura e ",pes[cdmra]," kgs.")
print("O cliente mais baixo foi o de codigo = ",cli[cdmna]," com ",alt[cdmna]," m de altura e ",pes[cdmna]," kgs.")
print("O cliente mais pesado foi o de codigo = ",cli[cdmrp]," com ",alt[cdmrp]," m de altura e ",pes[cdmrp]," kgs.")
print("O cliente mais leve foi o de codigo = ",cli[cdmnp]," com ",alt[cdmnp]," m de altura e ",pes[cdmnp]," kgs.")