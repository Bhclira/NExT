'''
Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total. Obs.: somente são vendidos um número inteiro de latas.
'''

area = int(input('Digite o tamanho da área a ser pintada em metros quadrados: '))
calculandoLitros = area/3
calculandoLatas = calculandoLitros/18
calculandoValor = int(calculandoLatas)*80
print(f'Para uma área a ser coberta de {area}, serão gastos {calculandoLitros:.2f} litros de tinta.')
print(f'Essa litragem confere a quantidade de {round(calculandoLatas)} latas de tinta.')
print(f'Calculando valor total a ser pago: R$ {calculandoValor}')

# cada lata = 18l
# valor lata = 80
# qual a quantidade de latas a serem compradas
# qual o preço total
