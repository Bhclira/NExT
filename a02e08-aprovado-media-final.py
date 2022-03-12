'''
Complete o código na celula abaixo para imprimir uma mensagem se o aluno foi Aprovado ou Reprovado
com base na sua média final.
tire por média a nota 5.0
'''

print('\n' + 'Olá, Aluno! Vamos verificar sua situação de aprovação ...' + '\n')

notaAluno = float(input('Digite sua nota: '))

if notaAluno >= 5 and notaAluno <= 10:
    print('\n' + 'Aprovado!')
elif notaAluno < 5 and notaAluno >= 0:
    print('\n' + 'Reprovado!')
else:
    print('\n' + 'Nota Inválida!')

print('\n' + '... FIM DO PROGRAMA.' + '\n')

'''
aprendi a restringir os dados fornecidos como entrada pelo usuário a um número válido
acrescentei para tanto limitantes dentro das estruturas do if-else para não aceitar
nem números negativos, nem números acima de 10
funcionou
'''