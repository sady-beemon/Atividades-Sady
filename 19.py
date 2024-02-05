"""Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.
Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
326 = 3 centenas, 2 dezenas e 6 unidades
12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16"""

import math
n1 = int(input("Digite um numero em até 1000 unidades: "))

c = int(round(n1/100,0))
d = int((n1-(c*100))/10)
u = int(n1 - (c*100) - d *10)

if n1 == 1000:
    print(n1," = 10 centenas.")
elif c == 1:
    if u == 0  and d == 0:
        print(n1," = Uma Centena.")
    elif d == 0:
        if u == 1:
            print(n1," = Uma Centena e Uma Unidade.")
        else:
            print(n1," = Uma Centena e ",u," Unidades.")
    elif u == 0:
        if d == 1:
            print(n1," = Uma Centena e Uma Dezena")
        else:
            print(n1," = Uma Centena e ", d ," Dezenas")
    else:
        if d == 1 and u == 1:
            print(n1," = Uma Centena ,Uma Dezena e Uma Unidade.")
        elif u == 1:
            print(n1," = Uma Centena ,",d," Dezenas e Uma Unidade.")
        elif d == 1:
            print(n1," = Uma Centena ,", d ," Dezena e ", u , " Unidades.")    
elif n1 > 100:
    if u == 0  and d == 0:
        print(n1," = ",c," Centenas.")
    elif d == 0:
        if u == 1:
            print(n1," = ",c," Centenas e Uma Unidade.")
        else:
            print(n1," = ",c," Centenas e ",u," Unidades.")
    elif u == 0:
        if d == 1:
            print(n1," = ",c," Centenas e Uma Dezena")
        else:
            print(n1," = ",c," Centenas e ",d," Dezenas")
    else:
        if d == 1 and u == 1:
            print(n1," = ",c," Centenas ,Uma Dezena e Uma Unidade.")
        elif u == 1:
            print(n1," = ",c," Centenas ,",d," Dezenas e Uma Unidade.")
        elif d == 1:
            print(n1," = ",c," Centenas ,Uma Dezena e ", u , " Unidades.")
        else:
            print(n1," = ",c," Centenas , ",d ," Dezenas e ", u , " Unidades.")
elif d == 1:
    if u == 0:
        print(n1, " =  Uma Dezena.")
    elif u == 1:
        print(n1, " = Uma Dezena e Uma Unidade.")
    else:
        print(n1, " = Uma Dezena e ", u ," Unidades.")
elif n1 > 10:
    if u == 0:
        print(n1, " = ", d, " Dezenas.")

    elif u == 1:
        print(n1, " = ", d, " Dezenas e Uma Unidade.")
    else:
        print(n1, " = ", d, " Dezenas e ", u ," Unidades.")
elif n1< 10:
    if u == 1:
        print(n1, " = Uma Unidade.")
    else:
        print(n1, " = ",u," Unidades.")