"""O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
                      Até 5 Kg           Acima de 5 Kg
File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, porém não há limites para a quantidade de carne por cliente. Se compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o total da compra. Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal, contendo as informações da compra: tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.
"""

tipo = int(input("Selecione o tipo de carne:\n1 - File Duplo\n2 - Alcatra\n3 - Picanha\n"))
kg = int(input("Digite a quantidade desejada(em Kg): "))

forma = int(input("Selecione a forma de pagamento:\n1- Dinheiro\n2- Cartao Tabajara(5% Disconto)\n3-Outro\n"))

if tipo == 1 :
    prc = kg*4.90
    if kg > 5:
        prc = kg* 5.80
    if forma == 1:
        print("Cupom Fiscal\n",
              "Tipo de carne: File Duplo.\n",
              "Quantidade comprada: ",kg," Kg.\n",
              "Preço total: R$",prc,".\n",
              "Forma de pagamento: Dinheiro.\n",
              "Preço Final: ",prc,"."
              )
    elif forma == 2:
        print("Cupom Fiscal\n",
              "Tipo de carne: File Duplo.\n",
              "Quantidade comprada: ",kg," Kg.\n",
              "Preço total: R$",prc,".\n",
              "Forma de pagamento: Cartao Tabajara.\n",
              "Preço Final: ",prc-(prc*0.05),".")
    elif forma == 3:
        print("Cupom Fiscal\n",
              "Tipo de carne: File Duplo.\n",
              "Quantidade comprada: ",kg," Kg.\n",
              "Preço total: R$",prc,".\n",
              "Forma de pagamento: Outro.\n",
              "Preço Final: ",prc,".")
elif tipo == 2 :
    prc = kg * 5.90
    if kg>5:
        prc = kg*6.80
    if forma == 1:
        print("Cupom Fiscal\n",
              "Tipo de carne: Alcatra.\n",
              "Quantidade comprada: ",kg," Kg.\n",
              "Preço total: R$",prc,".\n",
              "Forma de pagamento: Dinheiro.\n",
              "Preço Final: ",prc,"."
              )
    elif forma == 2:
        print("Cupom Fiscal\n",
              "Tipo de carne: Alcatra.\n",
              "Quantidade comprada: ",kg," Kg.\n",
              "Preço total: R$",prc,".\n",
              "Forma de pagamento: Cartao Tabajara.\n",
              "Preço Final: ",prc-(prc*0.05),".")
    elif forma == 3:
        print("Cupom Fiscal\n",
              "Tipo de carne: Alcatra.\n",
              "Quantidade comprada: ",kg," Kg.\n",
              "Preço total: R$",prc,".\n",
              "Forma de pagamento: Outro.\n",
              "Preço Final: ",prc,".")
elif tipo == 3:
    prc = kg * 6.90
    if kg>5:
        prc = kg * 7.80
        if forma == 1:
            print("Cupom Fiscal\n",
              "Tipo de carne: Picanha.\n",
              "Quantidade comprada: ",kg," Kg.\n",
              "Preço total: R$",prc,".\n",
              "Forma de pagamento: Dinheiro.\n",
              "Preço Final: ",prc,"."
              )
    elif forma == 2:
        print("Cupom Fiscal\n",
              "Tipo de carne: Picanha.\n",
              "Quantidade comprada: ",kg," Kg.\n",
              "Preço total: R$",prc,".\n",
              "Forma de pagamento: Cartao Tabajara.\n",
              "Preço Final: ",prc-(prc*0.05),".")
    elif forma == 3:
        print("Cupom Fiscal\n",
              "Tipo de carne: Picanha.\n",
              "Quantidade comprada: ",kg," Kg.\n",
              "Preço total: R$",prc,".\n",
              "Forma de pagamento: Outro.\n",
              "Preço Final: ",prc,".")