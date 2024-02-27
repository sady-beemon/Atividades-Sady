import pprint

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
            continue
        else:
            correct +=1
    if correct == 4:
        valido.append(list[i])
    else:
        invalido.append(list[i])

print("\nEndereçoes Validos:\n")
pprint.pprint(valido,width=1)
print("\nEndereçoes invalidos:\n")
pprint.pprint(invalido,width=1)