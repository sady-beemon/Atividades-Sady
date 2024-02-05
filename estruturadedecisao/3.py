"Faça um Programa que verifique se uma letra digitada é 'F'' ou 'M' Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido."

sexo = input("Insira seu genero:\nF - Feminino, M - Masculino")
if sexo == 'M':
    print("Masculino")
elif sexo =='F':
    print("Feminino")
else:
    print("Sexo Inválido")