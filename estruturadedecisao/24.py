"""Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
par ou ímpar;
positivo ou negativo;
inteiro ou decimal."""

n1 =  float(input("Digite o primeiro numero: "))
n2 =  float(input("Digite o segundo numero: "))
print("Digite a opçao desejada:",
                 "\n1 - Soma",
                 "\n2 - Subtraçao.",
                 "\n3 - Multiplicaçao.",
                 "\n4 - Divisao.\n"
                 )
desc = int(input())

if desc == 1:
    resul = n1 + n2
elif desc == 2:
    resul = n1 - n2
elif desc == 3:
    resul = n1 * n2
elif desc == 4:
    resul = n1 / n2

print("O resultado da equaçao é ", resul,
      "Este numero é:")
if resul%2==0:
    print("Um numero  par.")
else:
    print("Um numero impar.")

if resul > 0:
    print("Um numero positivo")
elif resul < 0:
    print("Um numero negativo")

if round(resul,0) != resul:
    print("Um numero decimal")
else:
    print("Um numero inteiro.")