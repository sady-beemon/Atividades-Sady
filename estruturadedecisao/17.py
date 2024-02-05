"Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto."

ano = int(input("Informe um ano: "))
bix = 0

while bix < ano:
    bix += 4

if bix == ano:
    print("O ano informado é bissexto")
else :
    print("O ano informado nao é bissexto")