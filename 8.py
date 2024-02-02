"Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato."
 
p1 = int(input("Digite o preço do primeiro produto:"))
p2 = int(input("Digite o preço do segundo produto:"))
p3 = int(input("Digite o preço do terçeiro produto:")) 

if p1 < p2 and p1<p3:
    print("O produto que voce deve comprar é o de ",p1," Reais.")
elif p2 < p1 and p2<p3:
    print("O produto  que voce deve comprar é o de ",p2," Reais.")
elif p3 < p2 and p3<p1:
    print("O produto  que voce deve comprar é o de ",p3," Reais.")
else:
    print("Os produtos tem o mesmo valor.")