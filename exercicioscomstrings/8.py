"""Palíndromo. Um palíndromo é uma seqüência de caracteres cuja leitura é idêntica se feita da direita para esquerda ou vice−versa. Por exemplo: OSSO e OVO são palíndromos. Em textos mais complexos os espaços e pontuação são ignorados. A frase SUBI NO ONIBUS é o exemplo de uma frase palíndroma onde os espaços foram ignorados. Faça um programa que leia uma seqüência de caracteres, mostre−a e diga se é um palíndromo ou não."""
ep = []
n = str(input("Digite uma frase: "))
for i in range(len(n)):
    if n[i] == ' ':
        False
    else:

        ep.append(n[i])

n = ''.join(ep)
n = str(n)
n.lower
print(n)
inv = (n[::-1])
if inv == n:
    print("A frase é um palindromo.")
else:
    print("A frase nao é um palindromo")