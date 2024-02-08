"""Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar se a média de idade da turma varia entre 0 e 25,26 e 60 e maior que 60; e então, dizer se a turma é jovem, adulta ou idosa, conforme a média calculada."""

n = int(input("Digite a quantidadede pessoas na turma: "))
idades =0

for i in range(n):
    idade =int(input("Digite a idade de cada pessoa: "))
    idades += idade
    media = idades / (i+1)

print("A media das notas é: ",media)
if media <=  25 and media > 0:
    print("A turma é jovem")
elif media <=60 and media >= 26:
    print("A turma Adulta.")
elif media > 60:
    print("A turma é Idosa.")