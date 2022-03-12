'''
Construa uma pequena CHAVE DICOTÔMICA para identificar uma planta como membro de um grupo
BRYOPHYTA
PTERIDOPHYTA
GYMNOSPERMAE
ANGIOSPERMAE

a identificação se dá com base na presença (1) oua ausencia (0) de três características:
1. vascularização
2. sementes]
3. flores

utilize tabela fornecida como referência...

'''

print('\n' + 'Bem vindo ao Identificador de grupo de Plantas!')
# usuário deve fornecer os 3 aspectos da planta que ele deseja analisar
print('\n' + 'Digite 0 para ausência ou 1 para presença dos seguintes aspectos: ')

vasc = (int(input('Para a vascularização da planta: ')))
sem = (int(input('Para as sementes da planta: ')))
flor = (int(input('Para as flores na planta: ')))

if vasc == 0 and sem == 0 and flor == 0:
    print('\nO gênero da Planta é: Briophyta')

elif vasc == 1 and sem == 0 and flor == 0:
    print('\nO gênero da Planta é: Pteridophyta')

elif vasc == 1 and sem == 1 and flor == 0:
    print('\nO gênero da Planta é: Gymnospoermae')

elif vasc == 1 and sem == 1 and flor == 1:
    print('\nO gênero da Planta é: Angiospermae')

else:
    print('\nERRO! O sistema só aceita 0 e 1, execute novamente o programa.')

print('\n' + '... FIM DO PROGRAMA' + '\n')