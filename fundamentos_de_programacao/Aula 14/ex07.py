ficha = []

while True:

    nome = str(input('Nome: ')).capitalize()
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2

    ficha.append([nome, [nota1, nota2], media])

    resp = str(input('Quer continuar? (s/n): '))
    if resp in 'Nn':
        break

print(ficha)
print()
print('-' * 26)
print(f'{"No.":<4}{"Nome:":<10}{"MEDIA":>8}')
print('-' * 26)

for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.2f}')

print('-' * 26)
print()

while True:
    print('-' * 58)
    opc = int(input('Mostrar notas de qual aluno? (999 - encerra programa): '))
    
    if opc == 999:
        print ('\nfinalizando ...')
        break
    
    if opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
    
print('... VOLTRE SEMPRE ...\n')