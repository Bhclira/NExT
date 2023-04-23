# for

'''
# range(10)
# range(0,10)
# range(0,10,1)
'''
acumulador = 0
lista = []

for i in range(1, 5, 1):
    num = int(input('Digite um Número: '))
    lista.append(num)
    acumulador += num

print(f'Valor do somatório dos digitados: {acumulador}')
print(f'Lista dos digitados: {lista}')
print(f'Maior número encontrado entre os digitados: {max(lista)}')
print(f'Menor número encontrado entre os digitados: {min(lista)}')

print('\nFim do programa')