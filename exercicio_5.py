# Peça ao usuário para digitar um número e faça a válidação de que o que foi digitado foi um número.

num = (input("Digite um número: "))
Cnum = num.isdigit()

while Cnum == False:
    num = input("Número inválido. \nDigite um número: ")
    Cnum = num.isdigit()

input("Pressione Enter para sair...")