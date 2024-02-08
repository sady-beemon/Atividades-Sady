"""Uma empresa de pesquisas precisa tabular os resultados da seguinte enquete feita a um grande quantidade de organizações:
"Qual o melhor Sistema Operacional para uso em servidores?"

As possíveis respostas são:

1- Windows Server
2- Unix
3- Linux
4- Netware
5- Mac OS
6- Outro
Você foi contratado para desenvolver um programa que leia o resultado da enquete e informe ao final o resultado da mesma. O programa deverá ler os valores até ser informado o valor 0, que encerra a entrada dos dados. Não deverão ser aceitos valores além dos válidos para o programa (0 a 6). Os valores referentes a cada uma das opções devem ser armazenados num vetor. Após os dados terem sido completamente informados, o programa deverá calcular a percentual de cada um dos concorrentes e informar o vencedor da enquete. O formato da saída foi dado pela empresa, e é o seguinte:
Sistema Operacional     Votos   %
-------------------     -----   ---
Windows Server           1500   17%
Unix                     3500   40%
Linux                    3000   34%
Netware                   500    5%
Mac OS                    150    2%
Outro                     150    2%
-------------------     -----
Total                    8800

O Sistema Operacional mais votado foi o Unix, com 3500 votos, correspondendo a 40% dos votos.
"""

vtt = 0
jg = ['Windows Server','Unix','Linux','Netware','Mac OS','Outro']
vts = [0,0,0,0,0,0]
mhl = -1000

while True:
    jgdr = int(input("Selecione o melhor sistema operacional na sua opniao:(selecionar de 1-6 ou 0 para sair) \n1- Windows Server\n2- Unix\n3- Linux\n4- Netware\n5- Mac OS\n6- Outro\n"))
    if jgdr == 0:
        break
    elif jgdr > 6:
        print("Informe um valor entre 1 e 6 ou 0 para sair!")
    else:
        vts[jgdr-1] += 1
        vtt += 1

for i in range(6):
    if vts[i] >= mhl:
        mhl = vts[i]
        pcm = i

print("Foram computados: ",vtt,"\n\nSistema Operacional     Votos   %")
for i in range(len(vts)):
    if vts[i] > 0:
        print(jg[i]," Votos: ",vts[i]," %",round(((vts[i]/vtt)*100),1))

print("O Sistema mais votado foi o : ",jg[pcm]," com %",round(((vts[pcm]/vtt)*100),1),"dos votos")
