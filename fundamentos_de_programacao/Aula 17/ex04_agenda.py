# for k, v in enumerate(dicionario) -> indexa o índice com a chave do dicionário

# PRATICAR:

agenda = {'Maria': [99887766, 99887755],
          'Pedro': [87654433],
          'Joaquim': [99887711, 99665533]}

print()
print(agenda.keys()) # retorna lista as chaves do dicionário
print()
print(agenda.items()) # retorna tupla com as chaves e valores do dicionário
print()
print(agenda.values()) # retorna uma lista com todos os valores do dicionário
print()

# iteração com dicionários (é feita apartir das chaves):
print('-' * 30)
print(f'{"KEY.":<10}{"VALUE.[1][2][3]... [n]":<20}')
for k, v in agenda.items():
    print(f'{k:<10}{v}')
        
print('-' * 30)
print()

while True:

    print('[1] Adicionar telefone a um contato')
    print('[2] Remover telefone de um contato')
    print('[3] Apagar contato')
    print('[4] Atualizar número')

    opc = int(input('\nDigite a opção desejada: '))

    if opc == 1:

        chaveAmodificar = input('Digite o nome do contato: ')
        newnumber = str(input(f'Digite novo número de {chaveAmodificar}: '))
        agenda[chaveAmodificar].append(newnumber)
    
    elif opc == 2:

        chaveAmodificar = input('Digite o nome do contato: ')
        print(agenda[chaveAmodificar])
        deletarNumber = int(input(f'Digite qual telefone irá remover [1][2][3]... [n]: '))
        agenda[chaveAmodificar].pop(deletarNumber -1)
        print(agenda[chaveAmodificar])
        
    elif opc == 3:

        chaveAmodificar = input('Digite o nome do contato: ')
        del agenda[chaveAmodificar]

    elif opc == 4:
        chaveAmodificar = input('Digite o nome do contato: ')
        atualizarNumber = int(input(f'Digite qual telefone irá atualizar [1][2][3]...[n]: '))
        newnumber = input('Digite o novo número: ')
        agenda[chaveAmodificar].pop(atualizarNumber - 1)
        agenda[chaveAmodificar].insert(atualizarNumber-1, newnumber)
   
    else:
        print('\n Digite um número válido de [1] a [4]')
        
    escolha = input('\n8Deseja Manipular mais algo na AGENDA? (s/n): ')

    if escolha in 'nN':
        break

print('\nAGENDA ATUALIZADA')
print('-' * 30)
print(f'{"KEY.":<10}{"VALUE.[1][2][3]...[n]":<20}')
for k, v in agenda.items():
    print(f'{k:<10}{v}')
        
print('-' * 30)
print()
print('...ENCERRANDO PROGRAMA...\n')