# Faça um programa que recebe do usuário 10 valores de números inteiros, armazena em um vetor e apos percorre-lo exibe qual é o maior valor e a sua posição.

n = 10
valores = []

print('\n')

for i in range (1, 11):
    valor = int(input(f'Valor {i}: '))
    valores.append(valor)

print('-' * 45)
print(valores)
print('-' * 45)
print(f'\nO MAIOR Valor Encontrado: {max(valores)}')
print(f'\nA posição do MAIOR VALOR: {valores.index(max(valores))}')
print('-' * 45)