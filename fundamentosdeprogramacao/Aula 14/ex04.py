vetor = []

while True:

    print()
    vetor.append(int(input(f'Digite um valor inteiro para adicionar à lista: ')))

    opc = input('Digite se quer adicionar mais um numero [S/N]: ')

    if opc in 'Nn':
        print(f'\nSua lista gerada foi: {vetor}\n')
        break

print(f'Valor da lista encontrado na posição 2 foi: {vetor[2]}')

while True:
    print()
    print(vetor)
    print()
    print('Você pode manipular sua lista a partir das opções abaixo: \n')
    print('[1] Substituir valor Existente: ')
    print('[2] Adicionar novo valor: ')
    print('[3] Saber quantidade de valores do vetor: ')
    print('[4] Adicionar um valor em um índice específico: ')
    print('[5] Remover valor pelo seu índice: ')
    print('[6] Remover um valor pelo seu conteúdo: ')
    print()

    
    opc = int(input('Digite a opção desejada: '))

    if opc == 1:
        
        index = int(input(f'Digite o índice do valor a ser substituído: '))
        new_value = int(input(f'Digite o valor novo: '))
        vetor[index] = new_value
        print(vetor)
    
    elif opc == 2:
        new_value = (int(input('Digite o número inteiro a acrescentar: ')))
        vetor.append(new_value)
        print(vetor)
    
    elif opc == 3:
        print(f'A quantidade de entidades do vetor é de: {len(vetor)}')
            
    elif opc == 4:
        
        index = int(input('Digite a posição em que deseja anexar o novo valor: '))
        new_value = int(input('Digite o novo valor: '))
        vetor.insert(index, new_value)
        print(vetor)
    
    elif opc == 5:
        index = int(input('Digite o índice do valor que deseja remover: '))
        vetor.pop(index)
        print(vetor)

    elif opc == 6:
        value = int(input('Digite o novo valor a ser substituido: '))
        vetor.remove(value)
        print(vetor)
    
    else:
        print('Digite um número válido entre 1 e 6!')


    alterar = str(input('\nSe deseja MODIFICAR + algo, escolha a opção (s/n): '))

    if alterar in 'nN':
        print('\n... PROGRAMA FINALIZADO ...\n')
        break