'''
Desenvolva um programa que receba (o usuário insere) cinco valores
inteiros e guarde em um vetor (lista). Ao final, mostre os valores na tela.
'''

lista = []

for i in range(5):
    lista.append(int(input('Digite Valor: ')))

print(f'Para {len(lista)} valores digitados: {lista}')