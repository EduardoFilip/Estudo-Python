a = int(input("Digite um número: "))
b = int(input("Digite outro número: "))

operacao = str(input("Qual operação você deseja realizar? \n Escolha uma das opções abaixo: \n M - Multiplicação \n D - Divisão \n S - Soma \n U - Subtracao \n "))

if operacao == 'M':
    operacao = a * b
    print("O resultado da operação é: {}" .format(operacao))
elif operacao == 'D':
    operacao = a / b
    print("O resultado da operação é: {}" .format(operacao))