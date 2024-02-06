"""Faça um programa que leia e valide as seguintes informações:
Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd';"""

while True:
    name = input("Digite um nome com mais de 3 letras:")
    idade = int(input("Digite uma idade entre 0 a 150 anos."))
    salario = int(input("Digite um salario maior que 0: "))
    sexo = input("'f' ou 'm': ")
    ec = input("Estado Civil: 's', 'c', 'v', 'd':")
    if len(name) > 3 and idade >= 0 and idade <= 150 and salario > 0 and (sexo == 'f' or sexo == 'm') and (ec == 's' or ec == 'c' or ec == 'v' or ec == 'd'):
        print("Informaçoes validas")
        break
    else:
        print("Informaçoes invalidas.")
