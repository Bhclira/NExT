'''
Uma escola te contratou para fazer um software em Python. Eles querem que você crie um script que exiba o seguinte menu:

    0. Sair
    1. Exibir lista de alunos com suas notas (cada aluno tem uma nota)
    2. Inserir aluno e nota
    3. Alterar a nota de um aluno
    4. Consultar nota de um aluno específico
    5. Apagar um aluno da lista

Implemente esse script usando um dicionário. O dicionário ao ser declarado já deverá ser inicializado com três alunos e sua nota.
'''

from ast import Break


alunos = {'joao': 10.0,
         'maria': 8.0,
         'jose': 6.5}

print("""
    0. Sair
    1. Exibir lista de alunos com suas notas (cada aluno tem uma nota)
    2. Inserir aluno e nota
    3. Alterar a nota de um aluno
    4. Consultar nota de um aluno específico
    5. Apagar um aluno da lista
    """)

opcao = int(input('Digite a opção desejada: '))

if opcao == 1:
    print(alunos)

elif opcao == 2:
    nome_aluno = input('Digite o nome do Aluno: ')
    nota_aluno = float(input('Digite a Nota do Aluno: '))
    alunos[nome_aluno] = nota_aluno
    print(alunos)

elif opcao == 3:
    nome_aluno = input('Digite o nome: ')
    if nome_aluno in alunos.keys():
        nova_nota = input('Nova Nota: ')
        alunos[nome_aluno] = nova_nota
    else:
        print ('Aluno não encontrado')

    print(f'\nNova Lista de Notas: {alunos}')

elif opcao == 4:
    nome_aluno = input('Digite o nome desejado: ')
    print(f'A nota do Aluno é: {alunos.get(nome_aluno, "chave não encontrada")}')

elif opcao == 5:
    nome_aluno = input('Digite o nome do aluno: ')
    if nome_aluno in alunos:
        del alunos[nome_aluno]
    else:
        print('Nome de Aluno não encontrado.')
    
    print(f'Lista atualizada {alunos}')

elif opcao == 0:
    Break