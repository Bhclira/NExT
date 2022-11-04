'''
ex11 - Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:

a. o produto do dobro do primeiro com metade do segundo.
b. soma do triplo do primeiro com o terceiro.
c. terceiro elevado ao cubo.
'''

num1 = int(input('\nDigite um primeiro número inteiro: '))
num2 = int(input('Digite um segundo número inteiro: '))
num3 = float(input('Digite um número real[decimal]: '))

# letra A
letra_A = (2*num1)*(num2/2)
letra_B = (3*num1)+num3
letra_C = num3**3

print(f'\nO produto do dobro do primeiro com metade do segundo é: {letra_A}')
print(f'A soma do triplo do primeiro com o terceiro é: {letra_B}')
print(f'terceiro elevado ao cubo é: {letra_C}\n')
