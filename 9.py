"Faça um Programa que leia três números e mostre-os em ordem decrescente."

n1 = int(input("Digite o primeiro numero:"))
n2 = int(input("Digite o segundo numero:"))
n3 = int(input("Digite o terçeiro numero:"))

if n1 > n2 and n1>n3:
    print(n1)
elif n2 > n1 and n2>n3:
    print(n2)
elif n3 > n2 and n3>n1:
    print(n3)
else:
    print("Os numeros tem o mesmo valor.")

if n1 > n2 and n1<n3 or n1<n2 and n1>n3:
    print(n1)
elif n2 > n1 and n2<n3 or n2<n1 and n2>n3:
    print(n2)
elif n3 > n2 and n3<n1 or n3<n2 and n3>n1:
    print(n3)


if n1 < n2 and n1<n3:
    print(n1)
elif n2 < n1 and n2<n3:
    print(n2)
elif n3 < n2 and n3<n1:
    print(n3)
else:
    print("Os numeros tem o mesmo valor.")

numbers = []
for i in range(3):
    number = int(input("Digite um numero:"))
    numbers.append(number)

numbers.sort()
print(" ",numbers[0],
      "\n",numbers[1],
      "\n",numbers[2])
