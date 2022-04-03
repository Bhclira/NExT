# Faça um programa que receba uma palavra e a imprima de tras-para-frente.
def inverter(txt):
    return txt[::-1]


palavra = input('\nDigite uma palavra qualquer: ')

# como função:
print(inverter(palavra))
print(f'\nFunção inverter: {inverter(palavra)}')

# usei o método slice
palavra = palavra[::-1]

print(f'\nInversão da palavra: {palavra}')