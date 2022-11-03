# Crie um programa que receba um valor inteiro e avalie se ele é positivo ou negativo. Essa avaliação deve ocorrer dentro de uma função que retorna um valor booleano.


def valida_numero(valor):
    if valor<0:
        return False
    else:
        return True

valor = int(input('\nDigite valor Real: '))

if valida_numero(valor)==True:
    print(f'\nNumero Positivo!\n')
else:
    print('\nNumero Negativo!\n')

# print(f'\nPara Número Positivo [TRUE] ou Para Número Negativo [FALSE]: {valida_numero(valor)}')