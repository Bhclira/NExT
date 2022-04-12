'''
Um distribuidor de refrigerantes vende seu produto em todo o país. Em cada trimestre do ano passado ele vendeu uma cenrta quantidade de garrafas em cada região do Brasil. Faça um algoritmo pra ler as quantidade vendidas e escfrever a quantidade total vendida em todo o país.

Pelo enunciado do problema, vimos que existem 20 dados de entrada, pois temos 4 trimestres no ano e cada trimestre teve uma venda para cada uma das cinco regioes do Brasil.
'''

matriz = [[], [], [], []]
soma = 0

for i in range (4):
    