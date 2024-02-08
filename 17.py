"""Em uma competição de salto em distância cada atleta tem direito a cinco saltos. O resultado do atleta será determinado pela média dos cinco valores restantes. Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos e depois informe o nome, os saltos e a média dos saltos. O programa deve ser encerrado quando não for informado o nome do atleta. A saída do programa deve ser conforme o exemplo abaixo:
Atleta: Rodrigo Curvêllo
 
Primeiro Salto: 6.5 m
Segundo Salto: 6.1 m
Terceiro Salto: 6.2 m
Quarto Salto: 5.4 m
Quinto Salto: 5.3 m

Resultado final:
Atleta: Rodrigo Curvêllo
Saltos: 6.5 - 6.1 - 6.2 - 5.4 - 5.3
Média dos saltos: 5.9 m"""

atleta = []

while True:
    nm = input("Digite os nomes dos atletas, ou 'sair' para sair do programa: ")
    saltos = []  
    maior = -1000
    menor = 1000
    media = 0
    if nm == 'sair':
        break
    for i in range(5):
        salto = float(input("Digite a distancia dos 5 saltos: "))
        if salto >= maior:
            maior = salto
        if salto <= menor:
            menor = salto
        
        media += salto
        saltos.append(salto)

    for i in range(len(saltos)):
        print("O salto ",i+1," teve uma distancia de: ",saltos[i]," metros.")

    print("\nMelhor salto: ",maior,
          "\nPior salto: ",menor,
          "\nMédia dos demais saltos: ",(media-(maior+menor))/3,
          "\n\nResultado final:\n",nm," : ",(media-(maior+menor))/3)
        
            