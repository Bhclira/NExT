vetor = []

while True:

    print()
    vetor.append(int(input(f'Digite um valor inteiro para adicionar à lista: ')))

    opc = input('Digite se quer adicionar mais um numero [S/N]: ')

    if opc in 'Nn':
        print(f'\nSua lista gerada foi: {vetor}\n')
        break

print(f'Valor da lista encontrado na posição 2 foi: {vetor[2]}')