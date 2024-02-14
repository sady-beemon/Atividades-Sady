"""Nome na vertical em escada invertida. Altere o programa anterior de modo que a escada seja invertida.

FULANO
FULAN
FULA
FUL
FU
F"""

n = str(input("Digite o nome do usuario: "))
rever = []
for i in range(len(n)):
    rever.append(n[i])
print(''.join(rever))
for i in range(len(n)):
    rever[(len(n)-1)-i] = ''
    print(''.join(rever))