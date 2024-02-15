"""Jogo da palavra embaralhada. Desenvolva um jogo em que o usuário tenha que adivinhar uma palavra que será mostrada com as letras embaralhadas. O programa terá uma lista de palavras lidas de um arquivo texto e escolherá uma aleatoriamente. O jogador terá seis tentativas para adivinhar a palavra. Ao final a palavra deve ser mostrada na tela, informando se o usuário ganhou ou perdeu o jogo."""

import random

palavras = ['abacaxi','fogao','peixe','mitocondria']
word = []
vida = 6
palavra = palavras[random.randint(0,3)]
p = list(palavra)
random.shuffle(p)
emb = ''.join(p)
for i in range(len(palavra)):
    word.append("-")
print("Jogo da forca:\nVidas = ",vida,".\nPalavra: ",emb)
while True:
    for i in range(len(palavra)):
        word[i] = "-"
    for i in range(len(palavra)):
        letra = str (input("Digite uma Letra: "))
        word[i] = letra
        print(word)

    print(''.join(word))
    if ''.join(word) == ''.join(palavra):
        print("Parabens! Voce acertou!")
        break
    elif vida <= 0:
        print("Oh nao! Voce perdeu.")
    else:
        vida = vida - 1
        print("Errou!!! Vidas = ",vida,
              "\nPalavra: ",emb)
