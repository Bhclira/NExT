# crie programa que acumule os preços digitados pelo usuário até que ele digite zero
# ao final imprima o valor acumulado com descontos de 10% para totais acima de 1000 reais

valor_total = 0
valor = int(input('\nDigite o valor do Produto, ou [0] para finalizar: '))

while valor != 0:
    
    if valor>0:
        valor_total = valor_total+valor
        valor = int(input('Digite um novo valor: '))
    else:
        print('Valor Inválido')
        valor_total = valor_total
        valor = int(input('Digite um novo valor: '))

if valor_total>1000:
    valor_total = valor_total* 0.9

print('Total R$', valor_total)