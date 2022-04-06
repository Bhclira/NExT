# Crie um programa que receba do usuário 5 números inteiros e os exiba
#   na tela na ordem contrária a que foi inserido.
# A leitura dos números deve ser feita em uma função e 
#   a exibição dos valores em ordem contrária deve ocorrer em outra função.

lista_numeros = []

for i in range(1, 6):
    num = int(input('Digite Numero: '))
    lista_numeros.append(num)


def inverter(lista_parametros):
    return lista_parametros[::-1]

print(inverter(lista_numeros))