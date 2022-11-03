'''
ex10 - Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit
formula: <(temC x 9/5) + 32 = 32 °F>
'''

tempC = float(input('\nBem-vindo! Vamos conveter a temperatura fornecida de Celsius para Farenheit, digite: '))

tempF = (tempC*(9/5))+32

print(f'\nA temperatura, em célsius, calculada foi de: {tempF:.2f} Graus Célsius\n')
