
valor_arvore = float(input('Digite o preço da árvore de natal escolhida: '))

qtd_enfeite_1 = int(input('Digite o número do enfeite 1 em questão comprados: '))
valor_enfeite_1 = float(input('Digite o valor do enfeite 1 em questão: '))
valor_enfeite_1 = qtd_enfeite_1*valor_enfeite_1

qtd_enfeite_2 = int(input('Digite o número do enfeite 2 em questão comprados: '))
valor_enfeite_2 = float(input('Digite o valor do enfeite 2 em questão: '))
valor_enfeite_2 = qtd_enfeite_2*valor_enfeite_2

qtd_enfeite_3 = int(input('Digite o número do enfeite 3 em questão comprados: '))
valor_enfeite_3 = float(input('Digite o valor do enfeite 3 em questão: '))
valor_enfeite_3 = qtd_enfeite_3*valor_enfeite_3

valor_total = valor_arvore + valor_enfeite_1 + valor_enfeite_2 + valor_enfeite_3
valor_rateio = (valor_total)/20

print(f'O valor total de compras do natal da empresa foi: R$ {valor_total}')
print(f'O valor para cada funcionário ficou: R$ {valor_rateio}')
