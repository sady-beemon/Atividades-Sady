"""O cardápio de uma lanchonete é o seguinte:
Especificação   Código  Preço
Cachorro Quente 100     R$ 1,20
Bauru Simples   101     R$ 1,30
Bauru com ovo   102     R$ 1,50
Hambúrguer      103     R$ 1,20
Cheeseburguer   104     R$ 1,30
Refrigerante    105     R$ 1,00
Faça um programa que leia o código dos itens pedidos e as quantidades desejadas. Calcule e mostre o valor a ser pago por item (preço * quantidade) e o total geral do pedido.
Considere que o cliente deve informar quando o pedido deve ser encerrado."""


cq = 0
bs = 0
bo = 0
hb = 0
cb = 0
rg = 0
print("""Especificação   Código  Preço
Cachorro Quente 100     R$ 1,20
Bauru Simples   101     R$ 1,30
Bauru com ovo   102     R$ 1,50
Hambúrguer      103     R$ 1,20
Cheeseburguer   104     R$ 1,30
Refrigerante    105     R$ 1,00""")
while True:
    cd = int(input("Digite o codigo do produto\nPara finalizar a compra digite um numero negativo: "))
    if cd < 0:
        break
    if cd == 100:
        cq += 1
    elif cd == 101:
        bs += 1
    elif cd == 102:
        bo += 1
    elif cd == 103:
        hb += 1
    elif cd == 104:
        cb += 1
    elif cd == 105:
        rg += 1

ttl = cb*1.2 + bs * 1.3 + bo*1.5+hb*1.2+cb*1.2+rg*1
print("O seu pedido foi:\n",
      "Chachorro quente: ",cq," R$ ",cq*1.2,
      "\nBauru simples: ",bs," R$ ",bs*1.3,
      "\nBauru com Ovo: ",bo," R$ ",bo*1.5,
      "\nHamburguer: ",hb," R$ ",hb*1.2,
      "\nCheeseburguer: ",cb," R$ ",cb*1.3,
      "\nRefrigerante: ",rg," R$ ",rg*1,
      "\n para um total de R$",ttl)
