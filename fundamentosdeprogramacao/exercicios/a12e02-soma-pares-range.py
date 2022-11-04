# Faça um programa que imprima a soma de todos os números pares entre
# dois números informados pelo usuário.

num1 = int(input('\nDigite o Primeiro Número: '))
num2 = int(input('Digite o Segundo Número: '))
soma = 0

for i in range (num1, num2):
    
    if i%2==0:
        print(f'{i}', end=' -> ')
        soma = soma + i

print(f'\nA soma dos Números Pares: {soma}')