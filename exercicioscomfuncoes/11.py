"""Data com mês por extenso. Construa uma função que receba uma data no formato DD/MM/AAAA e devolva uma string no formato D de mesPorExtenso de AAAA. Opcionalmente, valide a data e retorne NULL caso a data seja inválida.
"""

meses = ['Janeiro','Fevereiro','Abril','Março','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro']
def main():
    
    dia = int(input("Digite o dia: "))
    mes = int(input("Digite o mes"))
    ano = int(input("Digite o ano: "))
    resul = valid(dia,mes,ano)
    print(resul)

()
def valid(dia,mes,ano):
    if mes > 12 or mes < 1:
        print("Data invalida: ")
        quit()
    elif dia > 31 or dia < 1:
        print("Data invalida: ")
        quit()
    else:
        resul = extenso(dia,mes,ano)
        return resul
()
def extenso(dia,mes,ano):
    global meses
    dia =str(dia)
    ano = str(ano)
    resul = dia + ' de ' + meses[mes-1] + ' de ' + ano
    return resul

()

if __name__ == "__main__":
    main()