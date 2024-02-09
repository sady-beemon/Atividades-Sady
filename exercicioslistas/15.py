"""Faça um programa que leia um número indeterminado de valores, correspondentes a notas, encerrando a entrada de dados quando for informado um valor igual a -1 (que não deve ser armazenado). Após esta entrada de dados, faça:
Mostre a quantidade de valores que foram lidos;
Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
Calcule e mostre a soma dos valores;
Calcule e mostre a média dos valores;
Calcule e mostre a quantidade de valores acima da média calculada;
Calcule e mostre a quantidade de valores abaixo de sete;
Encerre o programa com uma mensagem;"""

n = []
cont = 0
cont7 = 0
s = 0
acm = 0

while True:
    nota = int(input("Digite quantas notas quiser: (para finalizar digite um numero negativo):"))
    if nota < 0:
        break
    n.append(nota)
    cont += 1
    s += nota
    if nota < 7:
        cont7 += 1

m = s/cont
print("A quantidade de valores que foram lidos; ",cont,
      "\nTodos os valores na ordem em que foram informados, um ao lado do outro: ",n)

n.reverse()
print("\nTodos os valores na ordem inversa à que foram informados, um abaixo do outro: ")
for i in range(len(n)):
    print(n[i])
    if n[i] > m:
        acm += 1

print("Calcule e mostre a soma dos valores: ",s,
"\nCalcule e mostre a média dos valores: ",m,
"\nCalcule e mostre a quantidade de valores acima da média calculada: ",acm,
"\nCalcule e mostre a quantidade de valores abaixo de sete: ",cont7,
"\n\nPrograma finalizado :: Obrigado por utilizar.")