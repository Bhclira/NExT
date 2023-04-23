# while

num = 1
while num != 0:
    num = int(input('Digite o número: '))
    if num > 0:
        print('NUMERO MAIOR QUE ZERO')
    elif num == 0:
        print('NUMERO IGUAL A ZERO')
    else:
        print('NUMERO NEGATIVO')

print('\nfim da execução\n')