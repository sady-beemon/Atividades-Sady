"""Faça um programa que leia uma quantidade indeterminada de números positivos e conte quantos deles estão nos seguintes intervalos: [0-25], [26-50], [51-75] e [76-100]. A entrada de dados deverá terminar quando for lido um número negativo."""
int1 = 0
int2 = 0
int3 = 0
int4 = 0

while True:
    n1 = int(input("Digite um numero que seja positivo: "))
    if n1 < 0:
        break
    if n1 >= 0 and n1 <= 25:
        int1 +=1
    elif n1 >= 26 and n1 <= 50:
        int2 +=1
    elif n1 >= 51 and n1 <= 75:
        int3 +=1
    elif n1 >=76 and n1 <= 100:
        int4 +=1
    print("[0-25]: ",int1," [26-50]: ",int2, "[51-75]: ",int3, " e [76-100]: ",int4)