"Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida."

dd = int(input("Digite um dia do mes: "))
mm = int(input("Digite o mes do ano: "))
aaaa = int(input("Digite o ano desejado: "))

if dd > 31 or dd < 0 or mm > 12 or mm < 0:
    print("A Data é invalida")
else:
    print("A Data é valida")