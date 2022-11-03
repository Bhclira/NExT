'''
ex09 - Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius

Fórmula <C = 5 * ((F-32) / 9)>
'''

tempF = float(input('\nBem-vindo! Vamos conveter a temperatura fornecida de Farenheit para Célsius, digite: '))

tempC = 5*((tempF-32)/9)

print(f'\nA temperatura, em célsius, calculada foi de: {tempC:.2f} Graus Célsius')
