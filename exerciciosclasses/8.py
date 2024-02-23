"""Classe Macaco: Desenvolva uma classe Macaco,que possua os atributos nome e bucho (estomago) e pelo menos os métodos comer(), verBucho() e digerir(). Faça um programa ou teste interativamente, criando pelo menos dois macacos, alimentando-os com pelo menos 3 alimentos diferentes e verificando o conteúdo do estomago a cada refeição. Experimente fazer com que um macaco coma o outro. É possível criar um macaco canibal?
"""

class macaco:
    def __init__(atributos, nome, estomago):
        atributos.nm = nome
        atributos.br = [estomago]
    def metodos(atributos):
        menu = int(input("Digite a açao desejada: \n1 - Comer\n2 - Ver estomago \n3 - Digerir\n"))
        if menu == 1:
            comer = str(input("Digite uma comida que este macaco comeu: "))
            atributos.br.append(comer)
        elif menu == 2:
            print(atributos.br)
        elif menu == 3:
            del atributos.br
            atributos.br = []
        print(f"O macaco {atributos.nm} esta com seu estomago cheio de {' , '.join(atributos.br)}.")
        

nome = str(input("Digite o nome do macaco: "))
comer = str(input("Digite uma comida que este macaco comeu: "))
mac = macaco(nome,comer)

while True:
    macaco.metodos(mac)
    cont = input("Deseja continuar?\n'sim'  'nao' : ")
    if cont == 'nao':
        break