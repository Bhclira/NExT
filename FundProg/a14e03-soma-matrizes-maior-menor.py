'''
a) a soma de todos os valores ímpares
b) a soma dos valores da primeira coluna
c)o menor valor da terceira linha
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
    print()