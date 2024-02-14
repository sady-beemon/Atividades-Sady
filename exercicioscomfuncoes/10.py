"""Jogo de Craps. Faça um programa de implemente um jogo de Craps. O jogador lança um par de dados, obtendo um valor entre 2 e 12. Se, na primeira jogada, você tirar 7 ou 11, você um "natural" e ganhou. Se você tirar 2, 3 ou 12 na primeira jogada, isto é chamado de "craps" e você perdeu. Se, na primeira jogada, você fez um 4, 5, 6, 8, 9 ou 10,este é seu "Ponto". Seu objetivo agora é continuar jogando os dados até tirar este número novamente. Você perde, no entanto, se tirar um 7 antes de tirar este Ponto novamente."""

import random

rdds = 0
def main():
    desc = str(input("Jogar dados: \nsim - nao: "))
    if desc == 'nao':
         quit()
    n = random.randint(2,12)
    print("dados: ",n)
    check(n)

()
def check(n):
    if n == 7 or n == 11:
        print("Voce é um natural e ganhou!")
        quit()
    elif n == 2 or n == 3 or n == 12:
        print("Voce perdeu(craps)!")
    else:
        print("Voce marcou  seu ponto: ",n)
        funcao(n)


()
def funcao(n):
        ponto = 0
        while ponto != n:
            desc = str(input("Jogar dados? \nsim - nao: "))
            if desc == 'nao':
                 quit()
            ponto = random.randint(2,12)
            print("Dados: ",ponto)
            if ponto == 7:
                 print(ponto," Voce perdeu.")
                 quit()
            elif ponto == n:
                 print("Voce ganhou!")
                 quit()

()

if __name__ == "__main__":
    main()
