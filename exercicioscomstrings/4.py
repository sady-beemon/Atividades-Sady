"""Nome na vertical em escada. Modifique o programa anterior de forma a mostrar o nome em formato de escada.

F
FU
FUL
FULA
FULAN
FULANO"""

n = str(input("Digite o nome do usuario: "))
rever = []
for i in range(len(n)):
    rever.append(n[i])
    print(''.join(rever))