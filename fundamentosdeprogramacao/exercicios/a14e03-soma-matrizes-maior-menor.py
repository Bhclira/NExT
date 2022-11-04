'''
a) a soma de todos os valores ímpares
b) a soma dos valores da primeira coluna
c) o menor valor da terceira linha
'''
import os
os.system('cls')

# criando lista vazia
matriz = [[], [], []]
soma_impar = soma_coluna = 0
# for para adicionar os valores
for linha in range (3):
    for coluna in range(3):
        matriz[linha].append(int(input(f'Insira valor da posição [{linha} {coluna}]: ')))

# for para mostrar a matriz
for linha in range(3):
    for coluna in range(3):
        print(f'[{matriz[linha][coluna]:⁴}]', end='')
        if matriz[linha][coluna]%2!=0:
            soma_impar+=matriz[linha][coluna]

    print()

# letra a
print(f'A soma dos valores ímpares é {soma_impar}')

# letra b
for linha in range(3):
    soma_coluna+=matriz[1][0]

print(f'A soma dos valores da primeira coluna é {soma_coluna}')

# letra c
for c in range(3):
    menor = min(matriz[2]) # linha 2

print(f'O menor valor da última linha é: {menor}')