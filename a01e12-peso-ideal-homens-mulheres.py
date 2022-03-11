'''
* pegue a altura de uma pessoa
* construa um algoritmo que calcule o peso ideal
* para homens: ((72.7*h) - 58)
* para mulheres: ((62.1*h) - 44.7)
'''

print('\nOlá! Vamos calcular seu peso ideal!\n')
altura = float(input('Digite sua altura em centímetros: '))
genero = str(input('Digite seu gênero [M] ou [F]: '))

if genero == 'm':
    pesoIdealHomem = float((72.7 * altura) - 58)
    print(f'\nSeu peso ideal é: {altura:.2f} kilogramas\n')

else:
    pesoIdealMulher = float((62.1*altura) - 44.7)
    print(f'\nSeu peso ideal é: {altura:.2f} kilogramas\n')

    '''
    * mais uma vez a fórmula apresenta mal funcionamento,
    * para tanto recebi na variável fim como float mas nao adiantou
    * usei o truncamento na variável de saída e funcionou com 2 casas
    '''

print('\n FIM DO PROGRMA\n')