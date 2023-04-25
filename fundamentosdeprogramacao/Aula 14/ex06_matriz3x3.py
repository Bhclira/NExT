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

for l in range(3):
    for c in range(3):
        matriz[l].append(int(input(f'Digite valores para a posição [{l} {c}]: ')))

for l in range(3):
    for c in range(3):
        print(f'[{matriz[l][c]:^4}]', end='')
        if matriz[l][c] % 2 != 0:
            somaImpar += matriz[l][c]
    print()

# a) A soma de todos os valores ímpares;


print(f'\nA soma dos número ÌMPARES encontrados foi: {somaImpar}')

for l in range(3):
    somaColuna1 = somaColuna1 + matriz[l][0]
print(f'\nA soma da primeira coluna foi: {somaColuna1}')

for l in range (3):
    if matriz[2][c] < menor:
        menor = matriz[2][c]
    else:
        menor = menor

print(f'Menor valor da terceira linha: {menor}')
