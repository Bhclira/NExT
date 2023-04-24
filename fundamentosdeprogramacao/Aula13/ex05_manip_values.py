# remova valor fornecido da lista, caso exista

valor = [1,2,4,6,8,10]

print(valor)
num = int(input('\nDigite valor a ser removido da lista acima: '))

if num in valor:
    valor.remove(num)
    print(f'Nova lista sem o número digitado {valor}')
else:
    print(f'o valor digitado: [{num}] não foi encontrado nem removido.')

print('\n final do programa.')