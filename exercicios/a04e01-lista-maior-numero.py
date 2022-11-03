# Faça um programa que leia 5 números e informe o maior número.

numeros = [1, 4, 7, 8, 0]

print(f'\nPara a lista: {numeros}')

print(f'\nO maior número da lista: {max(numeros)}')

print(f'O menor número da lista: {min(numeros)}\n')

# jeito 2

numero = []

for i in range(0,5):
    numero.append(int(input('Insira um Número: ')))

print(f'\nlista de inteiros obtidos: {numero}\n')
print(f'\nO maior número da lista: {max(numero)}')
print(f'O menor número da lista {min(numero)}\n\n')