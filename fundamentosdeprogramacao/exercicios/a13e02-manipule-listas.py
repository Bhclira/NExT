'''
Crie uma lista de valores reais com os seguintes números: 3.5, 6.7, 1.0, 4.9
Na sequência desenvolva um programa que:

a) Adicione o valor 2.3 na posição [1];
b) Remova o último valor da lista;
c) Substitua o valor do índice [2] por 9.2;
d) Ordene os valores em ordem crescente;
e) Print a quantidade de valores da lista;
f) Print a lista com os novos valores (mostre o índice e o valor).
'''

lista = [3.5, 6.7, 1.0, 4.9]
print(f'\nLista Original: {lista}')


# letra A
lista.insert(1, 2.3)    # Adiciona o VALOR no index, mantendo os demais
print (f'\nLista com Index adicionado na Posição 1: {lista}') 

# letra B
lista.pop()
print(f'\nLista sem o Último Valor: {lista}')

#letra C
lista[2] = 9.2  # cuidado! substituirá o valor antigo pelo novo
print(f'\nLista com Valor substituído na posição 2: {lista}')

# letra D
print(f'\nLista ordem crescente: {sorted(lista)}')
# print(f'\nLista Ordenada Crescente: {sorted(lista2)}')

# letra E
print(f'\nTamanho da Lista Atualizado: {len(lista)}\n')

# letra F
for i in range (len(lista)):
    print(f'Índice {i} - Valor {lista[i]}')

print('\n\n... Fim do Programa.\n')