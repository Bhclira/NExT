'''
Desenvolva um programa que crie uma matriz de dimensão 3x3.
O usuário insere os valores, e ao final, exiba a matriz na tela.
'''

# criando lista vazia
matriz = [[], [], []]


# for para adicionar os valores
for linha in range (3):
    for coluna in range(3):
        matriz[linha].append(int(input(f'Insira valor da posição [{linha} {coluna}]: ')))

# for para mostrar a matriz
for linha in range(3):
    for coluna in range(3):
        print(f'[{matriz[linha][coluna]:⁴}]', end='')

       

