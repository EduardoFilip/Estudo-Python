#Faça um programa que leia e valide as seguintes informações:
# Nome: maior que 3 caracteres;
# Idade: entre 0 e 150;
# Salário: maior que zero;
# Sexo: 'f' ou 'm';
# Estado Civil: 's', 'c', 'v', 'd';

nome = input("Digite seu nome: ")
while len(nome) <= 3:
    nome = input("O nome deve conter mais de 3 caracteres.\nDigite novamente seu nome: ")

idade = int(input("Digite sua idade: "))
while idade < 0 or idade > 150:
    idade = int(input("Idade inválida.\nDigite um valor entre 0 e 150: "))

salario = float(input("Digite o valor do seu salário: "))
while salario < 0:
    salario = float(input("Salário inválido.\n Digite seu salário novamente: "))

sexo = input("Qual seu sexo?\n Digite M para Masculino, F para Feminino ou N se não deseja informar: ")
while sexo != "M" and sexo != "m" and sexo != "F" and sexo != "f" and sexo != "N" and sexo != "n":
    sexo = input("Opção inválida.\nDigite M para Masculino, F para Feminino ou N se não deseja informar: ")
if sexo == "M" or "m":
    sexo = "Sexo Masculino"
elif sexo == "F" or sexo =="f":
    sexo = "Sexo Feminino"
else:
    sexo = "Sexo não informado"

estadoCivil = input("\nQual seu estado Cívil? \nDigite uma das opções abaixo: \nS - Solteiro(a) \nC - Casado(a) \nV -Viúvo(a) \nD - Divorciado(a)\n")
while estadoCivil != "S" and estadoCivil != "s" and estadoCivil != "C" and estadoCivil != "c" and estadoCivil != "V" and estadoCivil != "v" and estadoCivil != "D" and estadoCivil != "d":
    estadoCivil = input("\nOpção inválida. \nDigite uma das opções abaixo: \nS - Solteiro(a) \nC - Casado(a) \nV -Viúvo(a) \nD - Divorciado(a)\n")
if estadoCivil == "S" or estadoCivil == "s":
    estadoCivil = "Solteiro(a)"
elif estadoCivil == "C" or estadoCivil == "c":
    estadoCivil = "Casado(a)"
elif estadoCivil == "V" or estadoCivil == "v":
    estadoCivil = "Viúvo(a)"
else:
    estadoCivil = "Divorciado(a)"


opcao = input("\n Deseja ver seus dados cadastrados? \nDigite S para SIM ou N para Não:\n")
while opcao != "S" and opcao != "s" and opcao != "N" and opcao != "n":
    opcao = input("Opção inválida. \nDigite S para SIM ou N para Não:\n")
if opcao == "S" or opcao == "s":
    print("Seus dados armazenados são: \nNome: {}\nIdade: {} anos\nR$ {}\n{}\n{} " .format(nome, idade, salario, sexo, estadoCivil))
else:
    input("Pressione Enter para sair...")
input("\nPressione Enter para sair...")