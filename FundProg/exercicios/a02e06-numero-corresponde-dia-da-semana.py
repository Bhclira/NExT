'''
* faça um programa que leia o número e exiba o dia
* correspondente da semana. ex:
* 1 - domingo
* 2 - segunda
* 3 - terça e etc.
* caso digite um valor nao correspondente deve
* aparecer valor inválido
*
'''
print('\n' + 'Digite um número e saiba que dia da semana ele corresponde...' + '\n')
diaDaSemana = int(input('Digite um número inteiro [de 1 a 7]: '))

if diaDaSemana == 1:
    print('\nDomingo')
elif diaDaSemana == 2:
    print('\nSegunda')
elif diaDaSemana == 3:
    print('\nTerça')
elif diaDaSemana == 4:
    print('\nQuarta')
elif diaDaSemana == 5:
    print('\nQuinta')
elif diaDaSemana == 6:
    print('\nSexta')
elif diaDaSemana == 7:
    print('\nSábado')
else:
    print('\nNúmero não corresponde a um dia da semana válido. Tente novamente')

print('\n' + '... FIM DO PROGRAMA.' '\n')

'''
# uses if, elif, else
* aprendi que para atribuir valor à variável usei a sintaxe com 'igual'
* ao usar dentro do aninhamento if, elif, else
* percebi que não se trata de uma atribuição e sim de uma igualdade
* para tanto, tive que usar iguais duplicados para fazer a checagem
'''