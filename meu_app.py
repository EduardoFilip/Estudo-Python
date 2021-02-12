a = int(input("Digite um número: "))
b = int(input("Digite outro número: "))
mult = a * b
div = a / b
som = a + b
sub = a - b

operacao = input("Qual operação você deseja realizar? \n Escolha uma das opções abaixo: \n M - Multiplicação \n D - Divisão \n S - Soma \n U - Subtracao \n ")

if operacao == 'M' or operacao == 'm':
    print("O resultado da operação é: {} " .format(mult))
elif operacao == 'D' or operacao == 'd':
    print("O resultado da operação é: {} " .format(div))
elif operacao == 'S' or operacao == 's':
    print("O resultado da operação é: {} " .format(som))
elif operacao == 'U' or operacao == 'u':
    print("O resultado da operação é: {} " .format(sub))
else:
    print("Operação escolhida inválida!")
input("Pressione enter para fechar a janela...")