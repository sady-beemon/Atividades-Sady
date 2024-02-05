'''Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?" 
O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". 
Caso contrário, ele será classificado como "Inocente".'''

sus = 0

print("Responda com sim ou nao:\n")
p1 = str(input("Telefonou para a vítima? "))
if p1 == 'sim':
    sus += 1
p2 = str(input("Esteve no local do crime? "))
if p2 == 'sim':
    sus += 1
p3 = str(input("Mora perto da vítima? "))
if p3 == 'sim':
    sus += 1
p4 = str(input("Devia para a vítima? "))
if p4 == 'sim':
    sus += 1
p5 = str(input("Já trabalhou com a vítima?" ))
if p5 == 'sim':
    sus += 1

if sus == 2:
    print("Voce foi considerado Suspeito.")
elif sus == 3 or sus == 4:
    print("Voce foi considerado Cumplice.")
elif sus == 5: 
    print("Voce foi considerado Assassino.")
else:
    print("Voce foi considerado inocente.")