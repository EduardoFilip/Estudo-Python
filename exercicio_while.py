#Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.


nota = int(input("Digite um valor entre 0 à 10 : "))
while (nota < 0 or nota > 10):
    nota = int(input("Número inválido! \n  Digite um valor entre 0 à 10 : "))
input("Pressione enter para fechar a janela...")