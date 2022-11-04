'''
Preencher uma lista com 10 números inteiros, usando input;

○ Mostrar os valores armazenados na lista;
○ Informar o menor elemento da lista usando o min();
○ Informar o maior elemento da lista e seu índice usando max();
○ Informar quantos valores ímpares existem na lista.
'''

lista = []

for i in range(10):
    lista.append(int(input(f'Digite Inteiro {i+1}: ')))

# letra A
print(f'\nValores da Lista = {lista}')

# letra B
print(f'\nNúmero MÍNIMO encontrado: {min(lista)}')

# letra C
print(f'\n Número MÁXIMO encontrado: {max(lista)}')
print (f'{lista.index(max(lista))} ')

for i in range(len(lista)):
    if lista[i]%2!=0:
        print(f'Números ÍMPARES encontrados: {lista[i]}', end= ' -> ')
