"""Tamanho de strings. Faça um programa que leia 2 strings e informe o conteúdo delas seguido do seu comprimento. Informe também se as duas strings possuem o mesmo comprimento e são iguais ou diferentes no conteúdo.

Compara duas strings
String 1: Brasil Hexa 2006
String 2: Brasil! Hexa 2006!
Tamanho de "Brasil Hexa 2006": 16 caracteres
Tamanho de "Brasil! Hexa 2006!": 18 caracteres
As duas strings são de tamanhos diferentes.
As duas strings possuem conteúdo diferente."""

s1 = str(input("Digite a string 1: "))
s2 = str(input("Digite a string 2: "))
print('Tamanho de "Brasil Hexa 2006": ',len(s1))
print('Tamanho de "Brasil! Hexa 2006!": ',len(s2))
if len(s1) != len(s2):
    print("As duas strings são de tamanhos diferentes.")
elif len(s1) == len(s2):
    print("As duas strings são de tamanhos iquais.")

if s1 != s2:
    print("As duas strings possuem conteúdo diferente.")
elif s1 == s2:
    print("As duas strings possuem conteúdo iguais.")