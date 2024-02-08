"Faça um programa que calcule o mostre a média aritmética de N notas."

n = int(input("Digite a quantidade notas para calcular a media: "))
notas =0

for i in range(n):
    nota =int(input("Digite a nota: "))
    notas += nota
    media = notas / (i+1)

print("A media das notas é: ",media)