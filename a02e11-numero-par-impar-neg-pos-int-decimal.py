'''
faça um programa que leia dois números e em seguida pergunte ao usuário qual operação ele deseja realizar.
o resultado da operação deve ser acompanhado de uma frase que diga se o número é:
a. par ou impar
b. positivo ou negativo
c. inteiro ou decimal

obs. faça bonito.
'''

print('\n' + 'Bem vindo ao tipificador de números!\n')

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))

operacao = int(input('\nPara:\n 1. adição\n 2. subtração\n 3. multiplicação\n 4. divisão\n\nDigite a operação desejada: '))
resultado = 0

if operacao == 1:
    resultado = num1 + num2
    print('\nO resultado obtido foi: ', resultado, '\n')

elif operacao == 2:
    resultado = num1 - num2
    print('\nO resultado obtido foi: ', resultado, '\n')
elif operacao == 3:
    resultado = num1 * num2
    print('\nO resultado obtido foi: ', resultado, '\n')
elif operacao == 4:
    resultado = num1 / num2
    print('\nO resultado obtido foi: ', resultado, '\n')

if resultado%2 == 0: # se é par ou ímpar
    if resultado == round(resultado):
        print(f'{int(resultado)} é número PAR' + '\n') # imprima inteiro
    else:
         print(f'{resultado} é não é inteiro. Portanto não pode ser PAR ou IMPAR' + '\n')
else:
    if resultado == round(resultado):
        print(f'{int(resultado)} é número IMPAR' + '\n')
    else:
        print(f'{resultado} é não é inteiro. Portanto não pode ser PAR ou IMPAR' + '\n')

if resultado<0: # se é negativo ou positivo
        print(f'{resultado} é NEGATIVO' + '\n')
else: # se é positivo
    print(f'{resultado} é POSITIVO' + '\n')

if(resultado == round(resultado)): # se é inteiro ou decimal
    print(f'{int(resultado)} é um número INTEIRO')
else:
    print(f'{resultado} é um número DECIMAL')

print('\n' + '... FIM DO PROGRAMA' + '\n')

'''
pesquisei no stackoverflow como fazer a validação do decimal e inteiro
achei uma função chamada 'round' que resolveu minha lógica e
possibilitou a checagem da natureza do número pelo número que chagara
pela variável

percebi que o Python considera 'float' as operações entre inteiros. isso me fez aprender como receber uma variável float em inteiro


'''