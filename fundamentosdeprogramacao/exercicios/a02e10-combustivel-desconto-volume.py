'''
um posto está vendendo combustivel com a seguinte tabela de descontos:

ALCOOL
até 20 litros - 3%
acima de 20 litros - 5%

GASOLINA
até 20 litros - 4% por litro
acima de 20 litros - 6% por litro

escreva um aloritmo que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte forma: A-alcool; G-gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é 2.50 e o do álcool é 1,90

'''

print('Bem Vindo ao Posto da Quebrada!\nAqui você tem desconto na Gasolina e no Alcool!')
print('\n' + 'Alcool: 3 por cento até 20 litros ou 5 por cento acima de 20 litros')
print('Gasolina: 4 por cento até 20 litros ou 6 por cento por litro acima de 20 litros')
print('\n' + 'Abasteça com desconto! ')

valorAlcool = 1.90
valorGasolina = 2.50
valorTotal = 0

tipoCombustivel = str(input('Digite A para ALCOOL ou G para Gasolina: '))
litrosTotais = float(input('Digite quantos litros você deseja: '))

if tipoCombustivel == 'a':
    if litrosTotais < 20 and litrosTotais > 0:
        valorTotal = (valorAlcool - (valorAlcool*0.03)) * litrosTotais
        print(f'\nPara {litrosTotais} litros desejados, o valor final em R$: {valorTotal:.2f}\n')
    
    elif litrosTotais >= 20:
        valorTotal = (valorAlcool - (valorAlcool*0.05)) * litrosTotais
        print(f'\nPara {litrosTotais} litros desejados, o valor final em R$: {valorTotal:.2f}\n')
    else:
        print('\nNúmero de litros negativo indisponível para cálculo.\n')
elif tipoCombustivel == 'g':
    if litrosTotais < 20 and litrosTotais > 0:
        valorTotal = (valorGasolina - (valorGasolina * 0.04)) * litrosTotais
        print(f'\nPara {litrosTotais} litros desejados, o valor final em R$: {valorTotal:.2f}\n')
    
    elif litrosTotais >= 20:
        valorTotal = (valorGasolina - (valorGasolina * 0.06)) * litrosTotais
        print(f'\nPara {litrosTotais} litros desejados, o valor final em R$: {valorTotal:.2f}\n')
    else:
        print('\nNúmero de litros negativo indisponível para cálculo.\n')

print('\n' + 'Obrigado e Volte Sempre! ... FIM DO PROGRAMA.' + '\n')






