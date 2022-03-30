# Consultório. Insira nome, idade, e Se tem doença contagiosa.
# se tem 65 anos ou mais - prioritário
#   se tiver doença contagiosa - ala amarela
#   se nao, aula

import os

os.system("cls")

nome = input('\nDigite seu nome: ')
idade = int(input('Digite sua idade: '))
resp = input('VOCÊ POSSUI DOENÇA CONTAGIOSA? [sim] ou [nao]: ')

if idade >= 65:
    print('Atendimento Prioritário.\n')
    if resp == 'sim':
        print('Dirija-se à Sala AMARELA')
    else:
        print('Dirija-se à Sala BRANCA')

else:
    if resp == 'nao':
        print('Dirija-se à Sala AMARELA')
    else:
        print('Dirija-se à Sala BRANCA')
