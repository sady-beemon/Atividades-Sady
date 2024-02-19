"""Faça um programa que leia um arquivo texto contendo uma lista de endereços IP e gere um outro arquivo, contendo um relatório dos endereços IP válidos e inválidos.
O arquivo de entrada possui o seguinte formato:
200.135.80.9
192.168.1.1
8.35.67.74
257.32.4.5
85.345.1.2
1.2.3.4
9.8.234.5
192.168.0.256
O arquivo de saída possui o seguinte formato:
[Endereços válidos:]
200.135.80.9
192.168.1.1
8.35.67.74
1.2.3.4

[Endereços inválidos:]
257.32.4.5
85.345.1.2
9.8.234.5
192.168.0.256"""



list = []
part = []
valido = []
invalido = []
with open("1.txt","r") as arquivo:
    for linha in arquivo:
        list.append(linha.replace('\n',''))

print(list)
part = []
for i in range(len(list)):
    
    part = (list[i]).split('.')
    print(part)
    correct = 0
    for i2 in range(len(part)):
        num = part[i2]
        print(part[i2])
        if int(num) > 200 or int(num) <= 0:
            False
        else:
            correct +=1
    if correct == 4:
        valido.append(part)
    else:
        invalido.append(part)

print("Endereçoes Validos:\n")
for i in range(len(valido)):
    print(valido[i])
print("Endereçoes invalidos:\n")
for i in range(len(invalido)):
    print(invalido[i])