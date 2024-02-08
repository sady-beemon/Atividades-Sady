"Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes."

v = []
c = 0

for i in range(10):
    p = str(input("Digite uma sequencia de 10 letras."))
    if p == 'a' or p == 'e' or p == 'i' or p == 'o' or p == 'u':
        print("vogal")
    else:
        c += 1
        print("consoante")
        v.append(p)

print(c," consoantes forma lidas, sendo elas: ",v)