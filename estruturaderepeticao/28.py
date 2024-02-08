"""Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio gasto em cada um deles.
 O usuário deverá informar a quantidade de CDs e o valor para em cada um."""

cds = int(input("Digite a quantidade de CDs "))
prctl = 0

for i in range(cds):
    prc=float(input("Digite o preço de cada CD: "))
    prctl += prc
    media = prctl/(i+1)

print("O colecionador investiu: ",prctl," Reais em sua coleçao de ",cds," CDs\nTotalizando uma media de R$ ",int(media)," por CD.")