'''
peça um numero de ano e identifique se ele é ou não bissexto
'''
print('\nOlá! Vamos checar se o ano que você fornece é ou não BISSEXTO!')

ano = int(input('Digite o ano: '))

# um ano é bissexto quando: é múltiplo de 4 e (+), ao mesmo tempo, é divisível por 100
# ou quando é divisível por 400

if ((ano%4==0 and ano%100!=0) or (ano%400==00)):
    print(f'\nO ano {ano} é Bissexto.\n')
else:
    print(f'\nO ano {ano} NÃO é Bissexto.\n')