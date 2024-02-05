'''Um posto está vendendo combustíveis com a seguinte tabela de descontos:
Álcool:
até 20 litros, desconto de 3% por litro
acima de 20 litros, desconto de 5% por litro
Gasolina:
até 20 litros, desconto de 4% por litro
acima de 20 litros, desconto de 6% por litro Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina).
Calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.'''

cmb = str(input("Digite o codigo do tipo de combustivel:\nA-álcool, G-gasolina\n"))
qnt = int(input("Quanto litros do combustivel deseja? "))

if cmb == 'A':
    prc = qnt*1.90
    if qnt > 20:
        prc = prc - (prc*0.05)
    else:
        prc =prc - (prc*0.03)    
elif cmb == ('G','g'):
    prc = qnt*2.50
    if qnt > 20:
        prc = prc - (prc*0.06)
    else:
        prc = prc - (prc*0.04)
else:
    print("Combustivel ou Quantidade nao identificado")

print("A quantia a ser paga é de R$",prc)