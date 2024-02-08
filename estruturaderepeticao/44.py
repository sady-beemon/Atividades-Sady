"""Em uma eleição presidencial existem quatro candidatos. Os votos são informados por meio de código. Os códigos utilizados são:
1 , 2, 3, 4  - Votos para os respectivos candidatos 
(você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
5 - Voto Nulo
6 - Voto em Branco
Faça um programa que calcule e mostre:
O total de votos para cada candidato;
O total de votos nulos;
O total de votos em branco;
A percentagem de votos nulos sobre o total de votos;
A percentagem de votos em branco sobre o total de votos. Para finalizar o conjunto de votos tem-se o valor zero."""

c1 = 0
c2 = 0
c3 = 0
c4 = 0
vn = 0
vb = 0
vt = 0

while True:
    voto =  int(input("Digite em quer deseja votar:\nPara finalizar o conjunto de votos tem-se o valor zero.\n1 , 2, 3, 4  - Votos para os respectivos candidatos.\n5 - Voto Nulo\n6 - Voto em Branco\n"))
    
    if voto == 1:
        c1 +=1
    elif voto == 2:
        c2 == 1
    elif voto == 3:
        c3 += 1
    elif voto == 3:
        c4 += 1
    elif voto == 5:
        vn += 1
    elif voto == 6:
        vb += 1
    elif voto == 0:
        break
    vt += 1
print("Os votos ficaram: candidato 1: ",c1,
      "\nCandidato 2: ",c2,
      "\nCandidato 3: ",c3,
      "\nCandidato 4: ",c4,
      "\nTotal de Votos Nulos: ",vn,
      "\nTotal de Votos Brancos: ",vb,
      "\nA percentagem de votos nulos sobre o total de votos: ",(vn/vt)*100,"%",
      "\nA percentagem de votos em branco sobre o total de votos: ",(vb/vt)*100,"%",)