"""Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
  Média de Aproveitamento  Conceito
  Entre 9.0 e 10.0        A
  Entre 7.5 e 9.0         B
  Entre 6.0 e 7.5         C
  Entre 4.0 e 6.0         D
  Entre 4.0 e zero        E
"""

nota1 = int(input("Digite a primeira nota: "))
nota2 = int(input("Digite a segunda nota: "))
media = (nota1 + nota2)/2

if media >= 0 and media < 4:
    print("E\nReprovado")
elif media >= 4 and media < 6:
    print("D\nReprovado")
elif media >= 6 and media < 7.5:
    print("C\nAprovado") 
elif media >= 7.5 and media < 9:
    print("B\nAprovado")
elif media >= 9 and media <=10:
    print("A\nAprovado")