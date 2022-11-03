'''
Crie arquivo exemplo2.txt e adicione os inputs disciplina cursada e turma dos alunos.
'''

arquivo = open('exemplo2.txt', 'w')

disciplina = input('Qual disciplina você está cursando? ')
turma = input('\nQual a sua turma? ')

arquivo.write(disciplina + "\n")
arquivo.write(turma + "\n")
arquivo.close

print('\n\tExibindo Infos: ')
arquivo = open('exemplo2.txt', 'r')
dados = arquivo.read()
print(dados)
arquivo.close()