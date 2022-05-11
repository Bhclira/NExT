print('''Lista:
            Produto 1 - R$5,30
            Produto 2 - R$6,00
            Produto 3 - R$3,20
            Produto 4 - R$2,50

''')


qtde = int(input('Digite quantidade de produtos Desejados: '))
codigo = int(input('Digite codigo do Produto Desejado: '))

if codigo == 1:
    valor_parcial = qtde * 5.30

elif codigo == 2:
    valor_parcial = qtde * 6.00

elif codigo == 3:
    valor_parcial = qtde * 3.20

elif codigo == 4:
    valor_parcial = qtde * 2.50

else:
    print('Codigo Inválido')


if valor_parcial >= 40 or qtde >= 15:
    valor_final = valor_parcial - valor_parcial*0.15
    print(f'valor com desconto: {valor_final}')

else:
    print(f'valor sem desconto: {valor_parcial}')