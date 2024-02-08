"Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores."

v1 = []
v2 = []
v3 = []

for i in range(10):
    va = int(input("Digite um dos 10 valores do primeiro vetor: "))
    vb = float(input("Digite um dos 10 valores do segundo vetor: "))
    v1.append(va)
    v2.append(vb)
    v3.append(va)
    v3.append(vb)

print("Primeiro vetor: ",v1,
      "\nSegundo vetor: ",v2,
      "\nTerceiro vetor: ",v3)