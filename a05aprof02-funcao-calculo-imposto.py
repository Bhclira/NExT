# Faça um programa com uma função chamada somaImposto. 
# 
# A função possui dois parâmetros formais:

#   taxaImposto, que é a quantia de imposto sobre vendas expressa em porcentagem
#   custo, que é o custo de um item antes do imposto.
# 
#  A função “altera” o valor de custo para incluir o imposto sobre vendas.

custo = float(input('\nDigite o Valor do Produto: '))
taxaImposto = float(input('\nDigite o Percentual de Imposto sobre Venda: '))

taxaImposto = taxaImposto / 100

def somaImposto(valor_produto, taxa):
    
    precoFinal = valor_produto + (valor_produto * taxa)
    return precoFinal

print(f'\nPreço Final com adição de Impostos:\n {somaImposto(custo, taxaImposto)}\n')