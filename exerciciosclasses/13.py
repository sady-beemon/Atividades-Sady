"""Classe Funcionário: Implemente a classe Funcionário. Um empregado tem um nome (um string) e um salário(um double). Escreva um construtor com dois parâmetros (nome e salário) e métodos para devolver nome e salário. Escreva um pequeno programa que teste sua classe."""

class funcionario:
    def __init__(atributos, nome,sal):
        atributos.nm = nome
        atributos.sl = sal
    
    def escolha_metodo(atributos):
        choic = int(input("Digite sua escolha:\n1 - Mostrar informaçoes de funcionario.\n2 - Modificar informaçoes do funcionario.\n"))
        if choic == 1:
            funcionario.mostrar_atributos(atributos)
        elif choic == 2:
            funcionario.modificar_atributos(atributos)
        else:
            print("Opçao invalida")

    def mostrar_atributos(atributos):
        print(f"O funcionario de nome {atributos.nm} tem um salario de R$ {atributos.sl}.")

    def modificar_atributos(atributos):
            nome = str(input("Digite o nome do funcionario: "))
            sal = float(input("Digite o salario do funcionario: "))
            atributos.nm = nome
            atributos.sl = sal


nome = str(input("Digite o nome do funcionario: "))
sal = float(input("Digite o salario do funcionario: "))
func = funcionario(nome,sal)
while True:
    funcionario.escolha_metodo(func)    
    cont = input("Deseja continuar?\n'sim'  'nao' : ")
    if cont == 'nao':
        break