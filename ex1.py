'''
- Pela tabela a seguir, mostre a descrição e o preço do produto após a digitação do código pelo usuário. Se o produto não estiver cadastrado, emitir mensagem avisando. OBS: utilizar o Desvio Condicional de Múltipla Escolha.

| **Código** | **Descrição** | **Preço R$** |
| --- | --- | --- |
| 01 | Caneta | 1.20 |
| 02 | Lápis | 0.80 |
| 03 | Caderno | 4.50 |
| 04 | Borracha | 1.00 |
| 05 | Régua | 1.50 |
'''

print("| Código | Descrição | Preço R$ |")
print("| 01 | Caneta | 1.20 |")
print("| 02 | Lápis | 0.80 |")
print("| 03 | Caderno | 4.50 |")
print("| 04 | Borracha | 1.00 |")
print("| 05 | Régua | 1.50 |")

opcao = input("Informe o código do produto: ")

match opcao:
    case 1:
        print("| Caneta | 1.20 |")
    case 2:
        print("| Lápis | 0.80 |")
    case 3:
        print("| Caderno | 4.50 |")
    case 4:
        print("| Borracha | 1.00 |")
    case 5:
        print("| Régua | 1.50 |")