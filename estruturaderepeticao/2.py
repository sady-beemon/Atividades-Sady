"""Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações."""

print("User :  User \nPassword :  1234")
while True:
    key = float(input("Digite sua senha."))
    if key != 1234:
        print("Senha invalida.")
    else:
        print("Senha valida.")
        break