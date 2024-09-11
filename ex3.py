'''
- Crie um menu com as 4 operações matemáticas (soma, subtração, multiplicação e divisão) que devem ser executadas com 2 números reais (float) de acordo com a escolha (opção) do usuário:

Opcao = 1: soma dos 2 números.

Opcao = 2: subtração dos 2 números.

Opcao = 3: multiplicação dos 2 números.

Opcao = 4: divisão dos 2 números.
'''

# Estrutura de decisão match case

# Menu de opções (somas, subtrações ou multiplicações)

num1 = int(input("Digite um número inteiro: "))
num2 = int(input("Digite outro número inteiro: "))

print("[1] somar os números")
print("[2] subtrair os números")
print("[3] multiplicar os números")
print("[4] dividir os números")

opcao = int(input("Digite a opção que deseja efetuar [1-3]: "))

match opcao:
    case 1:
        print(num1 + num2)
    case 2:
        print(num1 - num2)
    case 3:
        print(num1 * num2)
    case 4:
        if (num2 == 0):
            print("Erro: divisão por 0")
        else:
            print(num1 / num2)
    case _:
        print("Inválido")