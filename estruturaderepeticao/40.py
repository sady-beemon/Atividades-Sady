"""Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito. Foram obtidos os seguintes dados:
Código da cidade;
Número de veículos de passeio (em 1999);
Número de acidentes de trânsito com vítimas (em 1999). Deseja-se saber:
Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
Qual a média de veículos nas cinco cidades juntas;
Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio.
"""

cid = []
vei = []
aci = []
mvei = 0
cont = 0
maci = 0
mraci = -1
mnaci = 10000000

for i in range(5):
    cidp = int(input("Digite o codigo da cidade."))
    veip = int(input("Digite o numero de veiculos de passeio desta cidade."))
    acip = int(input("Digite o numero de acidentes de transito nessa cidade."))
    mvei += veip
    if veip <=2000:
        maci += acip
        cont += 1
    if acip >= mraci:
        mraci = acip
        cd1 = i
    elif acip <= mnaci:
        mnaci = acip
        cd2 = i
    cid.append(cidp)
    vei.append(veip)
    aci.append(acip)

print("\nA lista de informaçoes formadas foi a seguinte:")
for i in range(cid):
    print("A cidade de codigo: ",cid[i]," possue ",vei[i]," veiculos de passeio e registrou ",aci[i]," acidentes de transito.")

print("A media de veiculos foi de: ",mvei/5)
print("A cidade que mais registrou acidentes foi a de codigo: ",cid[cd1]," que teve ",mraci," acidentes.")
print("A cidade que menos registrou acidentes foi a de codigo: ",cid[cd2]," que teve ",mnaci," acidentes.")
print("A media de acidentes das cidades com menos de 2000 veiculos foi de: ",maci/cont)
