'''
Desenvolva um programa que crie uma matriz de dimensão 3x3. O usuário
insere os valores, e ao final, exiba a matriz na tela.
'''
somaTerceiraLinha = 0
somaColuna1 = 0
somaImpar = 0
menor = 100
lista = []
matriz = [[], [], []]

for linha in range(3):
    for coluna in range(3):
        matriz[linha].append(int(input(f'Digite valores para a posição [{linha} {coluna}]: ')))
    print(matriz)

print()
for linha in range(3):
    for coluna in range(3):
        print(f'[{matriz[linha][coluna]:^4}]', end='')
        
        if matriz[linha][coluna] % 2 != 0:
            somaImpar += matriz[linha][coluna]
    print()

# soma de todos os valores ímpares;
print(f'\nA soma dos número ÌMPARES encontrados foi: [{somaImpar}]')

# soma dos valores de uma linha [0]
for linha in range(3):
    somaColuna1 += matriz[linha][0]

print(f'A soma da primeira coluna foi: {somaColuna1}')

# Menor valor da coluna 2
for linha in range (3):
    if matriz[linha][2] < menor:
        menor = matriz[linha][2]

print(f'Menor valor da terceira linha: {menor}\n')
