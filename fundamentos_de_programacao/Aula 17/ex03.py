# dict.fromkeys -> recebe uma sequencia de chaves e index um único valor
     sintaxe -> dict.fromkeys = (seq, valor)

# del agenda('Joaquim')
# agenda.pop('catarina', 'nao encontrado')
# len(dicionario) = qtde de chaves
# 23 in moedas.values
# agenda.clear()
# print(notas.intems()) > retorna tuplas
# print dicionario.keys() retorna uma lista
# print notas.values() retorna uma lista


cardapio = {'coxinha': 5, 'pastel': 4, 'suco': 3.5, 'bolo': 4.5}

print('\n', cardapio, '/n')

print('-' * 17)
print(f'{"Chave":<12}{"Valor":^6}')
for k,v in cardapio.items():
    print(f'{k:<12}{v:^6}')
print('-' * 17)
print()

while True:
      
      print('''Selecione uma opção:\n
            [1] Inserir item
            [2] Apagar Item
            [3] Modificar valor
            [4] Atualizar valor
            ''')

      escolha = int(input('Digite sua opção: '))

      if escolha == 1:
           nome = input('Digite NOME do produto: ')
           valor = input('Digite VALOR do produto: ')
           cardapio[nome] = valor

      elif escolha == 2:
           nome = input('Digite a chave a ser excluída: ')
           del cardapio[nome]
      
      elif escolha == 3:
           nome = input('Digite a chave do valor a ser modificada: ')
           newvalue = int(input('Digite o novo valor: '))
           cardapio[nome] = newvalue
      
      elif escolha == 4:
           nome = input('Digite o nome da chave do valor a ser modificado: ')
           newvalue = int(input('Digite o novo valor: '))
           cardapio.update({nome: newvalue})
      
      else:
           print('... Digite um número válido de [1] a [5] ...')
           
      opc = input('\nDeseja alterar mais algo no dict? (s/n): ')

      if opc in 'Nn':
           break

print('\nCARDAPIO ATUALIZADO')
print('-' * 17)
print(f'{"Chave":<12}{"Valor":^6}')
for k,v in cardapio.items():
    print(f'{k:<12}{v:^6}')
print('-' * 17)
print()