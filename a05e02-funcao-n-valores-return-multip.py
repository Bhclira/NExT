# Crie um programa que tenha uma função que receba uma lista de números inteiros e exiba todos os valores multiplicados por um valor inserido pelo usuário.


lista = [1,2,3,4,5]
n = int(input('Digite um Valor: '))

def multiplicador(lista_parametro, valor_usuario):
    for i in lista_parametro:
        print(f'{i*valor_usuario}')

multiplicador(lista, n)