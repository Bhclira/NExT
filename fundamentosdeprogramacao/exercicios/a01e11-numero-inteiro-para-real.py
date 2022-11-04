'''
* peça dois inteiros e um real
* A. calcule o produto do dobro do primeiro com metade do segundo
* B. calcule a soma do triplo do primeiro com o terceiro
* C. e o terceiro elevado ao cubo
*
'''

num1 = int(input('\nDigite o primeiro número INTEIRO: ' ))
num2 = int(input('Digite o segundo número INTEIRO: '))
num3 = float(input('Digite o terceiro número REAL: '))

# LETRA A
calculo1 = float((num1*2) * (num2/2))
# LETRA B
calculo2 = float((3 * num1) + (num3))
# LETRA C
calculo3 = float((num3**3))

print(f'\nO resultado para letra a foi: {calculo1}\n')
print(f'O resultado para letra B foi: {calculo2}\n')
print(f'O resultado para letra C foi: {calculo3:.1f}\n') # desejo truncar o resultado para 1 casa decimal

'''
* estou dando preferencia ao print formatado com a variável entre chaves
*  a sintaxe: "{calculo3:.2f}"
* usei a função expoente com a sintaxe python "numero**potencia"
'''