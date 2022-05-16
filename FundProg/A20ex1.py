'''
Usando a Função pré-definida math, faça um programa que receba do usuário um número positivo e diferente de zero, calcule e mostre:
a) Fatorial
b) Raiz Quadrada
c) Seno
d) Cosseno
e) Tangente
'''

import math

num = int(input('Digite um número positivo: '))

# A
print(f'Fatorial = {math.factorial(num)}')
# B
print(f'Raíz Quadrada = {math.sqrt(num)}')
# C
print(f'Seno = {math.sin(num)}')
# D
print(f'Cosseno = {math.cos(num)}')
#E
print(f'Tangente = {math.tan(num)}')