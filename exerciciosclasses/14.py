"""Aprimore a classe do exercício anterior para adicionar o método aumentarSalario (porcentualDeAumento) que aumente o salário do funcionário em uma certa porcentagem.
Exemplo de uso:
  harry=funcionário("Harry",25000)
  harry.aumentarSalario(10)"""

class funcionario:
    def __init__(atributos, nome,sal):
        atributos.nm = nome
        atributos.sl = sal

    def visualizar(atributos):

        print(f"O funcionario de nome {atributos.nm} tem um salario de R$ {atributos.sl}.")

    def aumentar_salario(atributos):
        porc = float(input("Digite a porcentagem do aumento: "))
        atributos.sl += atributos.sl*(porc/100)

    def mod_funcionario(atributos):
        nome = str(input("Digite o nome do funcionario: "))
        sal = float(input("Digite o salario do funcionario: "))
        atributos.nm = nome
        atributos.sl = sal

    def escolha(atributos):
        choic = int(input("Digite sua escolha:\n1 - Mostrar informaçoes de funcionario.\n2 - Modificar informaçoes do funcionario.\n3 - Aumtentar salario\n"))
        if choic == 1:
            funcionario.visualizar(atributos)
        elif choic == 2:
            funcionario.mod_funcionario(atributos)        
        elif choic == 3:
            funcionario.aumentar_salario(atributos)
        else:
            print("Opçao invalida")


nome = str(input("Digite o nome do funcionario: "))
sal = float(input("Digite o salario do funcionario: "))
func = funcionario(nome,sal)
while True:
    funcionario.escolha(func)    
    cont = input("Deseja continuar?\n'sim'  'nao' : ")
    if cont == 'nao':
        break