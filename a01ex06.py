'''
Faça um programa que peça o raio de um círculo, calcule e mostre a sua área.
'''

raio = float(input('\nDigite o raio do círculo em centímetros: '))
pi = 3.14

area = pi * (raio**2)

print(f'\n-> A área do referido triângulo é: {area} <-\n')

# fórmula da área: pi * r(ao quadrado)
# potenciação em python: x**y (x elevado a y)
# multiplicação: x * y (x vezes y)
# constante em python: FLOAT 