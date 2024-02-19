"""Quadrado mágico. Um quadrado mágico é aquele dividido em linhas e colunas, com um número em cada posição e no qual a soma das linhas, colunas e diagonais é a mesma. Por exemplo, veja um quadrado mágico de lado 3, com números de 1 a 9:

8  3  4 
1  5  9
6  7  2
Elabore uma função que identifica e mostra na tela todos os quadrados mágicos com as características acima. Dica: produza todas as combinações possíveis e verifique a soma quando completar cada quadrado. Usar um vetor de 1 a 9 parece ser mais simples que usar uma matriz 3x3.
"""
quadrado = [[],[],[]]
import random
def main():

    stop = 0

    while True:
        
        if  stop == 1:
            break
        else:
            cond = []
            quadrado = [[],[],[]]
            for i in range(3):
                i2 = 0
                while True:
                    if i2 == 3:
                        break 
                    n = random.randint(1,9)
                    print(n)
                    if n not in cond:
                        quadrado[i].append(n)
                        cond.append(n)
                    else:
                        i2 = i2 -1
                    i2 += 1
        print(quadrado)
        stop = funcao(quadrado)

    for i in range(3):
        print(quadrado[i])

def funcao(matriz):

    if matriz[0][0] + matriz[1][0] + matriz[2][0] == matriz[0][1] + matriz[1][1] + matriz[2][1] == matriz[0][2] + matriz[1][2] + matriz[2][2] == matriz[0][0] + matriz[0][1] + matriz[0][2] == matriz[1][0] + matriz[1][1] + matriz[1][2] == matriz[2][0] + matriz[2][1] + matriz[2][2] == matriz[0][0] + matriz[1][1] + matriz[2][2] == matriz[0][2] + matriz[1][1] + matriz[2][0]:
        return 1
    
if __name__ == "__main__":
    main()