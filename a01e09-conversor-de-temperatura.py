'''
* faça um programa que peça a temperatura em Fahrenheit,
* transforme em Celsius e
* mostre o resultado na tela
'''

print('\n' + 'Calcule temperatura Farenheit em Celsius: ' + '\n')

farenheit = float(input('Digite a temperatura em Farenheit: '))

celsius = 5 * ((farenheit - 32) / 9)

print(f'\nO resultado da conversão: {celsius:.2f}' + ' Graus Célsius\n')

'''
* aprendi a truncar o número através do print formatado
* sintaxe: "{variável:.2f}" - onde 2f = número de casas após a vírgula
* fonte: condigos do StackOverflow
*
* também existe esta outra forma sem o print formatado:
* "print('O valor de pi formatado é {:.2f}'.format(pi))"
'''