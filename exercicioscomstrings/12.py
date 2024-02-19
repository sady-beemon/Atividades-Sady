"""Valida e corrige número de telefone. Faça um programa que leia um número de telefone, e corrija o número no caso deste conter somente 7 dígitos, acrescentando o '3' na frente. O usuário pode informar o número com ou sem o traço separador.

Valida e corrige número de telefone
Telefone: 461-0133
Telefone possui 7 dígitos. Vou acrescentar o digito três na frente.
Telefone corrigido sem formatação: 34610133
Telefone corrigido com formatação: 3461-0133"""


form = []
tel = str(input("Digite um numero de telefone: "))
if len(tel) != 9:
    print("Telefone possui 7 dígitos. Vou acrescentar o digito três na frente: ")
    tel = f'3{tel}'
print("Telefone corrigido sem formatação: ",tel)
    
for i in range(len(tel)):
    form.append(tel[i])
    if tel[4] != '-':
        if i == 3:
            form.append('-')
    newtel =''.join(form)

print("Telefone corrigido com formatação: ",newtel)