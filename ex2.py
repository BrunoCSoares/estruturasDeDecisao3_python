'''
- Baseado em um número real X (float) digitado pelo usuário, utilize o desvio condicional de múltipla escolha e faça as seguintes operações:

Opcao = 1: adicione 5 ao valor de X e exiba na tela.

Opcao = 2: subtraia 4 ao valor de X e exiba na tela.

Opcao = 3: dobre o valor de X e exiba na tela.
'''

num = float(input("Informe um número: "))

opcao = input("Escolha de [1-3]: ")

match opcao:
    case 1:
        print(num + 5)
    case 2:
        print(num - 4)
    case 3:
        print(num * 2)
