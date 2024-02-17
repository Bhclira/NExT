'''
Desenvolva um programa que receba as notas de 5 alunos e, na
sequência calcule e informe a média;
Além disso, mostre na tela as notas que são superiores a média da turma.
'''

notas = []
acima_da_media = []
media = 0
for i in range (5):
    notas.append(float(input(f'Digite nota {[i+1]} de {[5]}: ')))

media = sum(notas)/len(notas)
print(f'Média das notas digitadas: {sum(notas)/len(notas)}')

for i in range (5):
    if notas[i] > media:
        print('A nota', notas[i], 'foi maior que a média')

print('\nprograma encerrado')