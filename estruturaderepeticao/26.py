"""Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. 
Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato."""

n = int(input("Digite a quantidadede de eleitores: "))
can1 =0
can2 = 0
can3 =0
for i in range(n):
    elei=int(input("Selecione um candidato :\n1 - candidato1   2 - candidato2   3 - candidato3"))
    if elei == 1:
        can1 += 1
    if elei == 2:
        can2 +=1
    if elei == 3:
        can3 +=1

print("Candidato1 : ",can1," Votos.",
      "\nCandidato2 : ",can2," Votos.",
      "\nCandidato3 : ",can3," Votos.",)