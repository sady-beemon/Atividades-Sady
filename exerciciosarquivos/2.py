"""A ACME Inc., uma empresa de 500 funcionários, está tendo problemas de espaço em disco no seu servidor de arquivos. Para tentar resolver este problema, o Administrador de Rede precisa saber qual o espaço ocupado pelos usuários, e identificar os usuários com maior espaço ocupado. Através de um programa, baixado da Internet, ele conseguiu gerar o seguinte arquivo, chamado "usuarios.txt":
alexandre       456123789
anderson        1245698456
antonio         123456456
carlos          91257581
cesar           987458
rosemary        789456125
Neste arquivo, o nome do usuário possui 15 caracteres. A partir deste arquivo, você deve criar um programa que gere um relatório, chamado "relatório.txt", no seguinte formato:
ACME Inc.               Uso do espaço em disco pelos usuários
------------------------------------------------------------------------
Nr.  Usuário        Espaço utilizado     % do uso

1    alexandre       434,99 MB             16,85%
2    anderson       1187,99 MB             46,02%
3    antonio         117,73 MB              4,56%
4    carlos           87,03 MB              3,37%
5    cesar             0,94 MB              0,04%
6    rosemary        752,88 MB             29,16%

Espaço total ocupado: 2581,57 MB
Espaço médio ocupado: 430,26 MB
O arquivo de entrada deve ser lido uma única vez, e os dados armazenados em memória, caso sejam necessários, de forma a agilizar a execução do programa. A conversão da espaço ocupado em disco, de bytes para megabytes deverá ser feita através de uma função separada, que será chamada pelo programa principal. O cálculo do percentual de uso também deverá ser feito através de uma função, que será chamada pelo programa principal."""

"""user = []
space = []
ttl = 0

func = []

with open("usuarios","w") as arquivo:
    for linha in arquivo:
        func.append(arquivo.readlines(''))
    ttl = len(arquivo)

media = ttl/len(user)

for i in range(len(user)):
    print(i+1," - ",user[i]," espaço utilizado: ",space[i]," Porcentagem: ",round((space[i]/ttl)*100,1))

print("Espaço total ocupado: ",ttl,
      "\nEspaço médio ocupado: ",media)"""

def conversao(by):
    mb = round((int(by) /1048576),2)
    return(mb)

ttl = 0
medio = 0
list = []
with open("2.txt","r") as arquivo:
    for linha in arquivo:
        
        list.append(((linha.replace(' ',':')).replace('\n','')).split(':'))

for i in range(len(list)):
    list[i][1] = conversao(list[i][1])
    ttl += list[i][1]

medio = ttl / len(list)
with open("Resultados.txt","w") as resul:
    resul.write("Nr.  Usuário        Espaço utilizado     % do uso\n")
    for i in range(len(list)):
        text = f'{i+1}  {list[i][0]}  {list[i][1]} MB {(list[i][1]/ttl)*100} %\n'
        resul.write(text)

    text2 = f'\nEspaço total ocupado: {ttl}MB\nEspaço médio ocupado: {medio} MB'
    resul.write(text2)