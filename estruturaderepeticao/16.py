"A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,... Faça um programa que gere a série até que o valor seja maior que 500."

s = [1,1]
i = 0
clc = 0
while clc < 500:
    clc = s[i] + s[i+1]
    s.append(clc)
    i += 1

print(s)
