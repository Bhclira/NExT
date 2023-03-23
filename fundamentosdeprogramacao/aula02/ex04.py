print ('\nResponda as questões abaixo com 0 para NÃO ou 1 para SIM: ')

vasc = int(input('\nA planta possui VASCULARIZAÇÃO? (sim ou não): '))
semente = int(input('\nA planta possui SEMENTES? (sim ou não): '))
flor = int(input('\nA planta possui FLORES? (sim ou não): '))

if vasc == 0 and semente==0 and flor==0:
    print('\nBryophyta')

if vasc == 1 and semente==0 and flor==0:
    print('\nPteridophyta')

if vasc == 1 and semente == 1 and flor == 0:
    print('\nGymnospermae')

if vasc == 1 and semente == 1 and flor == 1:
    print('\nAngiospermae')

else:
    print('\nCombinação fora de sequenciamento. Programa encerrado.\n')