'Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.'

tempo = input("Digite o turno em que coçe estuda:\nM-matutino ou V-Vespertino ou N- Noturno")

if tempo == 'M':
    print("Bom Dia!")
elif tempo == 'V':
    print("Boa Tarde!")
elif tempo == 'N':
    print("Boa Noite!")
else:
    print("Valor Inválido!")