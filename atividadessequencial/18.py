"""Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps).
Calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos)."""


mb = int(input("Digite o tamanho do arquivo em 'mb': "))
mbs = int(input("Digite a velocidade de dowload do link de acesso em 'mbs': "))
print("O tempo de dowload do arquivo é de: ",(mb/mbs)/60," minutos.")