"""Valida e corrige número de telefone. Faça um programa que leia um número de telefone, e corrija o número no caso deste conter somente 7 dígitos, acrescentando o '3' na frente. O usuário pode informar o número com ou sem o traço separador.

Valida e corrige número de telefone
Telefone: 461-0133
Telefone possui 7 dígitos. Vou acrescentar o digito três na frente.
Telefone corrigido sem formatação: 34610133
Telefone corrigido com formatação: 3461-0133"""

tel = (input("Digite um numero de telefone: "))
newtel = []

if len(tel) > 9:
    print("Numero de telefone precisa ter 8 digitos: ")
    for i in range(8):

        if tel[i] ==any('0','1','2','3','4','5','6','7','8','9') or tel[4] == '-':
            newtel.append(tel[i])
        else:
            print("Numero em posiçao ",i+1," invalido substituido por: ",i)
            tel[i] == i
    if tel[4:] != '-':
        newtel[4] = '-'

print(newtel)