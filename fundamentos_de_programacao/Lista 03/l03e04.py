
time1 = str(input('Digite o nome do primeiro time: '))
gols_time1 = int(input(f'Digite o número de gols marcados pelo {time1}: '))

time2 = str(input('Digite o nome do segundo time: '))
gols_time2 = int(input(f'Digite o número de gols marcados pelo {time2}: '))

if (gols_time1 > gols_time2):
    print(f'\nO vencedor foi: {time1.upper()}\n')

elif (gols_time2 > gols_time1):
    print(f'\nO vencedor foi: {time2.upper()}\n')

elif (gols_time1 == gols_time2):
    print('EMPATE'\n)