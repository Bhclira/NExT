# palíndromo = palavra igual se for escrita de trás pra frente
# lista.split(' ') -> devolve uma lista com strings das palavras da frase
# lista = ''.join(lista) -> adiciona, juntando as strings da lista nova em uma outra string única
# lista[::-1] -> lê a lista de string única de trás pra frente. ou de posição [-1] até [0]

while True:

    frase = str(input('Digite uma frase: ')).lower()

    # tratando a frase antes da análise dos dados

    frase = frase.split(' ') # para remover todos os caracteres 'espaço' + criar lista com cada palavra como string
    print (f'\nA frase quebrada em string depois do "split()": {frase}\n')
    frase = ''.join(frase) # join junta o conteúdos da lista em uma string única
    print(f'Frase em forma de string única depois do join: {frase}\n')

    if frase == frase[::-1]:
        print(f'Sua resposta: a frase digitada é SIM um Palíndromo!')
        print()

    else:
        print(f'Sua resposta: a frase digitada NÃO é Palindromo')
        print()
    
    opc = str(input('Deseja verificar se outra frase é um PALÍNDROMO? (s/n): '))

    if opc in 'Nn':
        print('\n ... ENCERRANDO PROGRAMA ...\n')
        break

