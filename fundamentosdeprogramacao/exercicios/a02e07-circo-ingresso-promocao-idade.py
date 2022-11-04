'''
crie um programa para um circo, no qual dada a idade da pessoa, seja indicado o valor do ingresso segundo às regras:
a. menos de 4 anos e maior que 60 - gratuito
b. entre 4 e 18 anos custa 20 reais
c. maior de 18 custa 30 reais
d. estudantes e professores pagam meia-entrada -() considere 30 reais para inteira e 15 para meia
'''

print('\n' + 'Bem vindo ao Circo!!! Entre com sua idade para saber qual o valor do seu ingresso ...')

valorIngresso = 0

meiaEntrada = int(input('\nSe você for estudante ou Professor, digite 1\ncaso contrário: digite 0 (zero): '))

if meiaEntrada == 1:
    valorIngresso = 15
    print('\n' + 'Bem vindo! Você tem direito a Meia-Entrada!')
    print(f'valor do ingresso com desconto é de: {valorIngresso} reais')

elif meiaEntrada == 0:
    idade = int(input('\nAgora, digite sua idade: '))
    
    if idade < 4 or idade > 60:
        print('\nParabéns! Hoje tem promoção e você foi classificado pela idade!')
        print(f'valor do ingresso: {valorIngresso} reais')

    if 4 <= idade <= 18:
        valorIngresso = 20
        print(f'\nvalor do ingresso: {valorIngresso} reais')
    
    if 18 <= idade < 60:
        valorIngresso = 30
        print(f'\nvalor do ingresso: {valorIngresso} reais')
else:
    print('\nNúmero inválido. Tente novamente!')

print('\n ... FIM DO PROGRAMA.\n')

'''
na syntaxe do bloco if, aprendi que é diferente do portugol
onde nós precisávamos usar '()'

usei uma variável com valor zerado no início para simplificar
meu trabalho no interior dos escopos condicionais: funcionou.

* tentei, sem sucesso, fazer uma lógica onde pedisse um numero inteiro
* e o programa checasse pelo tipo - se nao fosse inteiro, que o programa
* aplicasse a meia-entrada e não consegui (perguntar ao professor)

'''