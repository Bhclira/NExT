'''
* calcular as raízes de uma equação do segundo grau na forma "ax2 + bx + c"
* o programa deverá pedir os valores de a, b, c
* informe ao usuário o seguinte:

A - se usuário informar "a" igual a zero, a equação deixa de ser de segundo grau
e o programa não deve pedir os demais valores, sendo encerrado

B - se o "delta" for negativo, a equação não possui raízes reais.
informe ao usuário e encerre o programa

C - se "delta" igual a 0, a equação possui apenas uma raíz real; informe.

D - se o "delta" for positivo, a equação possui duas raízes reais; informe.
*
'''

import math

a = int(input('\nInforme o coeficiente a: '))

if (a==0):
    print('A equação não é de segundo grau.\n Programa encerrado!')

else:
    b = int(input('Digite o valor do coeficiente b: '))
    c = int(input('Digite o valor do coeficiente c: '))

    delta = b**2 - (4*a*c)

    if (delta < 0):
        print('\nDelta menor que zero. A equação não possui raízes reais.')
        print('\n... FIM DO PROGRAMA\n')   
    elif (delta == 0):
        raiz = -b / (2*a)
        print(f'Para Delta = 0, raíz = {raiz}')
    else:
        raiz1 = (-b + math.sqrt(delta)) / (2*a)
        raiz2 = (-b - math.sqrt(delta)) / (2*a)

        print(f'\nSão raízes da equação: {raiz1} e {raiz2}')
        print('\n... FIM DO PROGRAMA\n')
