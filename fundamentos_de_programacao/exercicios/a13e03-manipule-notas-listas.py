'''
Desenvolva um programa que receba as notas de 5 alunos e, na
sequência
A) Calcule e informe a média;
B) Além disso, mostre na tela as notas que são superiores a média da turma.
'''

notas = []

# percorra e adicione na lista os valores inseridos a cada iteração
for i in range(5):
    print(notas.append(float(input(f'Digite Nota {i+1} do Aluno: '))))

# calcule e mostre a média da lista completa
media = sum(notas)/len(notas)
print(f'\nMédia Obtida: {media}\n')

# percorra a lista e valide condição se nota maior que média
for i in range(len(notas)):
    if notas[i] > media:
        print(f'a Nota {i+1} = {notas[i]} é maior que a média {media}')

print('\n\n...Fim do Programa.\n')