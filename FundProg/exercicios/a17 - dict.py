# Usando uma lista
listaNomesTels = ['maria', [99887766, 99887755], 'pedro', [92345678], 'joaquim', [99887711, 99665533]]

    # acessar números de maria

# telDeMaria = listaNomesTels[listaNomesTels.index('maria')+1]
        # nao entendi a sintaxe do '+1'
# print(telDeMaria)

# Usando duas listas

listaNomes = ['maria', 'pedro', 'joaquim']
listaTelefones = [[99887766, 99887755], [92345678], [99887711, 99665533]]
   
    # como acessar os números de maria?

telDeMaria = listaTelefones[listaNomes.index('maria')]
        # metodo index retorna um inteiro da posição na lista 01 que equivale a posição na lista 02

# print (telDeMaria)

'''
Dicionário (Item) : Chave (KEY) + Valor (Value)
# chave funciona como o Index
# conteúdos podem ser qualquer coisa (ou outros dict)
# a chave é separada do seu valor por :
# cada par (chave+valor) é separado por ,
'''

   # acessando itens do dicionário
agenda = {'maria':[99887766, 99887755],
            'pedro':[92345678],
            'joaquim': [99887711, 99665533]}

# print(agenda)

# print(agenda['pedro'])
# print(agenda['joaquim'])

# print(agenda('ana')) 
        # retorna type error caso nao haja chave correspondente

 
'''
Os dicionários possuem um método específico para busca de valores, get(), no qual podemos passar como parâmetros a chave que queremos e um valor padrão para retornar caso essa chave não seja encontrada.
'''

# print (agenda.get('ana', 'chave não encontrada'))
        # caso nao ache a chave, retorna valor do segundo parametro
# print (agenda.get('pedro', 'chave não encontrada'))


# alterando o valor do conteúdo em dict()

agenda['pedro'] = [87654433]
    # substitui o valor encontrado na chave pedro pelo novo valor, alterando o dict

# print(agenda)
# acrescentando novos itens no dict

agenda['teresa'] = [65443322]
    # use chave não existente para acrescentar novo item ao final do dicionário

print(agenda)

# removendo valores do dicto (comando del)

# del agenda['joaquim']
# print(agenda)

# removendo valores do dicto (comando pop)

# print(agenda.pop('catarina', 'nao encontrado'))
# print(agenda.pop('teresa', 'não encontrado'))

# print(agenda)

# tamanho do dicto

idades = {'joao': 10, 'maria': 12, 'alice': 4}
# print(len(idades))

# verificando itens no dicionário

# print('thiago' in agenda) # retorna verdadeiro ou Falso
# print('maria' in agenda)
# print([87654433] in agenda)
# print([87654433] in agenda.values())

# removendo todos os elementos do dicto

# print(idades)
# idades_criancas = idades
# # idades.clear()

# print(idades)
# print(idades_criancas)

# acessando dicionários (comando keys)

notas = {'joao': [9.0, 8.0], 'maria': [10.0]}

# print(notas.keys())

# # acessando dicionarios (comando values)

# print(notas.values())

# criando dicts usando .fromkeys - atribui a n chaves o mesmo valor

# pessoas = dict.fromkeys(['joao','maria'], 20)
# print (pessoas)
# pessoas = dict.fromkeys(['pedro', 'jorge'], [20, 30])
# print (pessoas)

# percorrendo dicionarios - iteração feita a partir das chaves

notas = {'joao': [9.0, 8.0],
         'maria': [10.0, 2.0],
         'pedro': [8.5, 5,0]}

for nome in notas:
    media = sum(notas[nome]) / len(notas[nome])
    print(f'A média de {nome} é {media}')