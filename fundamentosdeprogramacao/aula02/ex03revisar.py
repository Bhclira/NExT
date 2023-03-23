level = int(input('Digite o Level do Voltorb: '))

if level >= 1 and level <= 20:
    print(f'Potencia de Choque do Trovão: {20 + level**3}')

elif level >= 21 and level<= 40:
    print(f'Potencia de Choque do Trovão: {8000 + (level - 10)**2}')

elif level >= 41 and level <= 60:
    print(f'Potencia de Choque do Trovão: {9000 + (5 * level)}')

elif level >= 61 and level <= 80:
    print(f'Potencia de Choque do Trovão: {9300 + (2 * level)}')

elif level >= 81 and level <= 100:
    print(f'Potencia de Choque do Trovão: {9500 + level}')

else:
    print('Esse não foi um Level Válido')