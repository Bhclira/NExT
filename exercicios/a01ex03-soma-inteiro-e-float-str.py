'''
3. Faça um programa que peça dois números e imprima a soma.
'''

num1 = float(input('Digite primeiro número: '))
num2 = int(input('Digite segundo número: '))

resultado = num1 + num2

print('\nA soma dos valores é: ' + str(resultado))
print('A soma dos valores é: %i' %(resultado)) # pesquisar %
print(f'A soma dos valores é: {resultado}')
print(resultado)

# float soma com int com dominância de float