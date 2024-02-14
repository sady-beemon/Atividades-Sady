"""Número por extenso. Escreva um programa que solicite ao usuário a digitação de um número até 99 e imprima-o na tela por extenso."""

dezenas = ['Vinte','Trinta','Quarenta','Cinquenta','Sessenta','Setenta','Oitenta','Noventa']
unidades = ['um','dois','tres','quatro','cinco','seis','sete','oito','nove']
dez = ['Dez','Onze','Doze','Treze','Quatorze','Quinze','Dezesseis','Dezessete','Dezoito','Dezenove']
n = input("Digite  um numero de 0 até 99: ")
if int(n) >= 0 and int(n) <100:
        
    if int(n) == 0:
        print("Zero")
    elif int(n) < 10:
        print(unidades[int(n)-1])
    elif int(n) >= 10 and int(n) < 20:
        print(dez[int(n)-10])
    elif round((int(n)/10),0) == int(n)/10:
        print(dezenas[int(n[0])-2])
    else:
        print(dezenas[int(n[0])-2]," e ",unidades[int(n[1])-1])