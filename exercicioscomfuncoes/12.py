"""Embaralha palavra. Construa uma função que receba uma string como parâmetro e devolva outra string com os carateres embaralhados. Por exemplo: se função receber a palavra python, pode retornar npthyo, ophtyn ou qualquer outra combinação possível, de forma aleatória. Padronize em sua função que todos os caracteres serão devolvidos em caixa alta ou caixa baixa, independentemente de como foram digitados.

"""
import random
def main():

    plv = str(input("Digite uma string como parametro: "))
    inv = funcao(plv)
    print("A palavra embaralhada ficou: ",inv)

()
def funcao(plv):
    p = list(plv)
    random.shuffle(p)
    emb = ''.join(p)
    return(emb)
    

()

if __name__ == "__main__":
    main()