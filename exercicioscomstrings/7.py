"""Conta espaços e vogais. Dado uma string com uma frase informada pelo usuário (incluindo espaços em branco), conte:

quantos espaços em branco existem na frase.
quantas vezes aparecem as vogais a, e, i, o, u."""

n = str(input("Digite uma frase: "))
branco = 0
vogal = 0


for i in range(len(n)):
    if n[i] == ' ':
        branco += 1
    elif n[i] == 'a' or n[i] == 'u' or n[i] == 'o' or n[i] == 'i' or n[i] == 'e':
        vogal += 1

print("A frase tem ",branco," espaços em branco e,",vogal," vogais.")