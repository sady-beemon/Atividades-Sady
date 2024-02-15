"""Jogo de Forca. Desenvolva um jogo da forca. O programa terá uma lista de palavras lidas de um arquivo texto e escolherá uma aleatoriamente. O jogador poderá errar 6 vezes antes de ser enforcado.

Digite uma letra: A
-> Você errou pela 1ª vez. Tente de novo!

Digite uma letra: O
A palavra é: _ _ _ _ O

Digite uma letra: E
A palavra é: _ E _ _ O

Digite uma letra: S
-> Você errou pela 2ª vez. Tente de novo!"""

import random

palavras = ['Abacaxi','Fogao','Peixe','Uva','Mitocondria']
word = []
vida = 6
palavra = palavras[random.randint(0,4)]

for i in range(len(palavra)):
    word.append("-")
print("Jogo da forca:\nVidas = ",vida,".\n")
while True:
    acerto = 0
    letra = str (input("Digite uma Letra: "))
    for i in range(len(palavra)):
        if letra == palavra[i]:
            str(word[i]).lower = letra.lower
            acerto = 1
    if acerto == 1:
        print("Acertou! Vidas = ",vida)
    else:
        vida = vida - 1
        print("Errou!!! Vidas = ",vida)
    print(''.join(word))
    if ''.join(word) == ''.join(palavra):
        print("Parabens! Voce acertou!")
        break
    elif vida <= 0:
        print("Oh nao! Voce perdeu.")
        break
    
