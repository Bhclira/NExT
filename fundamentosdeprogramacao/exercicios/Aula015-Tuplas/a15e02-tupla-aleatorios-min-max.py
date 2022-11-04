'''
Crie programa que vai gerar cinco números aleatórios (entre 0 e 100) e coloque em uma tupla

a) mostre a listagem de números gerados
b) mostre o maior número gerado
c) mostre o menor número gerado
'''

from random import randint

# nome_tupla.append(randint(0,100)) (comando dentro de um loop)

tupla = []
counter = 0

while counter < 5:
    tupla.append(randint(0,100))
    counter += 1

# A
print(f'Números Aleatórios Sorteados: {tupla}')

# B
print(f'Máximo: {max(tupla)}')

# C
print(f'Mínimo: {min(tupla)}')