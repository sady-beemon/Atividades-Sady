"""Uma fruteira está vendendo frutas com a seguinte tabela de preços:
                      Até 5 Kg           Acima de 5 Kg
Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total.
Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.
"""

maca = int(input("Digite a quantidade desejada de maças(em Kg):"))
morango = int(input("Digite a quantidade desejada de morangos(em Kg):"))

if morango <= 5 :
    prcmr = morango *2.50
elif morango > 5:
    prcmr = morango *2.20
if maca <= 5:
    prcmc = maca * 1.80
elif maca > 5:
    prcmc = maca *1.50

prc = prcmc + prcmr

if (morango +maca) >= 8 or prc >= 25:
    prc = prc - (prc*0.1)

print("O preço a ser pago é de R$: ",prc)