"A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a série até o n-ésimo termo."

s = [1,1]
n = int(input("Digite o a quantidade de termos que deseja gerar(Com base [1,1]):"))

for i in range(n):
    clc = s[i] + s[i+1]
    s.append(clc)

print(s)