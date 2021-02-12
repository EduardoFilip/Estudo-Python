#Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.

userName = input("Digite seu nome: ")
userPassword = input("Digite sua senha: ")

while (userPassword == userName):
    userPassword = input("Sua senha não pode ser igual ao nome de usuário! Digite novamente: ")

input("Pressione enter para sair...")