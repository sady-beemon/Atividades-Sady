"Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação."

while True:

    a = int(input("Digite a quantidade de pessoas na cidade A: "))
    b = int(input("Digite a quantidade de pessoas na cidade B: "))
    ano = 0
    ta = float(input("Digite a taxa de crescimento anual da cidade A (Em %) "))
    tb = float(input("Digite a taxa de crescimento anual da cidade B (Em %) "))

    while a < b:
        a += (a*(ta/100))
        b += (b*(tb/100))
        ano += 1

    print("Para a populaçao de A ultapassar a populaçao de B Se passaram: ", ano," anos.\n",
        "Com as populaçoes aumentando para um total de ", int(a) , " pessoas no pais A.\n",
        "E ",int(b)," pessoas no pais B.")
    
    r = str(input("Deseja repetir o programa? \nsim - nao\n"))
    if r == 'sim':
        break
