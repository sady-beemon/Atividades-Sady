"""Quadrado mágico. Um quadrado mágico é aquele dividido em linhas e colunas, com um número em cada posição e no qual a soma das linhas, colunas e diagonais é a mesma. Por exemplo, veja um quadrado mágico de lado 3, com números de 1 a 9:

8  3  4 
1  5  9
6  7  2
Elabore uma função que identifica e mostra na tela todos os quadrados mágicos com as características acima. Dica: produza todas as combinações possíveis e verifique a soma quando completar cada quadrado. Usar um vetor de 1 a 9 parece ser mais simples que usar uma matriz 3x3."""

import random
print("\t***** Quadrado Mágico *****\n ")
n=int(input("Informe o número central: "))
n_magico=n*3
print("O número mágico é: ",n_magico)
lvalor=[]
inicio=n-4
fim=inicio+8
print("Conforme o valor informado, temos os seguintes valores para preencher o Quadrado Mágico:\n")
while inicio<=(fim):
    lvalor.append(n-(n-inicio))
    print(n," - ",(n-inicio)," = ",n-(n-inicio))
    inicio=inicio+1
print("\nLista de valores: ", lvalor,"\n")
print("Nome das posições:")
c=1
while c<=9:
    print(c-1,end='\t')
    if c%3==0:
        print('\n')
        c+=1
print('\n')
print("Os valores para os cantos devem ser :",lvalor[1],lvalor[3],lvalor[5],lvalor[7])
pripos=4
print("Índice do centro= ",pripos)
listafinal=[0,0,0,0,0,0,0,0,0]
listafinal[pripos]=n
l=[0,2,6,8]
segpos=random.choice(l)
print("Sorteia o índice de um dos quatro cantos= ",segpos)
if segpos==0:
    tercpos=8
if segpos==2:
    tercpos=6
if segpos==6:
    tercpos=2
if segpos==8:
    tercpos=0
print("Posição oposta ao canto sorteado =",tercpos)
listafinal[segpos]=lvalor[1]
listafinal[tercpos]=lvalor[7]
l.remove(segpos)
l.remove(tercpos)
quartpos=random.choice(l)
print("Sorteia o índice de um dos cantos restantes =",quartpos)
listafinal[quartpos]=lvalor[3]
l.remove(quartpos)
quintpos=l[0]
print("Último canto =",quintpos,"\n")
listafinal[quintpos]=lvalor[5]
listafinal[1]=n_magico-(listafinal[0]+listafinal[2])
listafinal[3]=n_magico-(listafinal[0]+listafinal[6])
listafinal[5]=n_magico-(listafinal[8]+listafinal[2])
listafinal[7]=n_magico-(listafinal[6]+listafinal[8])
print("\nMatriz formada: \n")
c=1
while c<=9:
    print(listafinal[c-1],end='\t')
    if c%3==0:
        print('\n')
        c+=1
print('\n')