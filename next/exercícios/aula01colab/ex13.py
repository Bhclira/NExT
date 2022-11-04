'''
ex13 - Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
Para homens: (72.7*h) - 58
Para mulheres: (62.1*h) - 44.7
'''

altura = float(input('\nPara o cálculo do peso ideal, Digite uma altura[decimal]: '))

pesoHomem = (72.7*altura)-58
pesoMulher = (62.1*altura)-44.7

print(f'Para Homem, seu peso ideal seria de: {pesoHomem}\nPara mulher, seu peso ideal seria de: {pesoMulher}\n')
