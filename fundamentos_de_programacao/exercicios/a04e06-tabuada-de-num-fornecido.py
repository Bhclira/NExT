# Faça um programa que recebe um número de 1 a 10 do usuário e imprime a tabuada de multiplicação desse número

num = int(input('\nDigite um Número para Saber Sua Tabuada: '))

print('-' * 45)

for i in range (1, 11):
    print(f'{num} x {i} = {num*i}')

print('-' * 45)