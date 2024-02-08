"""Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente"."""

p = ["Telefonou para a vítima? ","Esteve no local do crime? ","Mora perto da vítima? ","Devia para a vítima? ","Já trabalhou com a vítima? "]
sus = 0

print("Responda com sim ou nao:\n")
for i in range(len(p)):
    res=input(p[i])
    if res == 'sim':
        sus += 1

if sus == 2:
    print("Voce foi considerado Suspeito.")
elif sus == 3 or sus == 4:
    print("Voce foi considerado Cumplice.")
elif sus == 5: 
    print("Voce foi considerado Assassino.")
else:
    print("Voce foi considerado inocente.")