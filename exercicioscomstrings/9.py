"""Verificação de CPF. Desenvolva um programa que solicite a digitação de um número de CPF no formato xxx.xxx.xxx-xx e indique se é um número válido ou inválido através da validação dos dígitos verificadores edos caracteres de formatação."""

cpf = str(input("Digite um CPF: "))
correct = 0

if len(cpf) == 14:
    if cpf[3] == '.':
        correct += 1
    if cpf[7] == '.':
        correct += 1
    if cpf[11] == '-':
        correct +=1
    for i in range(len(cpf)):
        if i == 3 or i == 7 or i == 11:
            False
        elif int(cpf[i]) >= 0:
            correct += 1
        print(cpf[i])

if correct == 14:
    print("Cpf valido.")
else:
    print("Cpf invalido.")
    print(correct)