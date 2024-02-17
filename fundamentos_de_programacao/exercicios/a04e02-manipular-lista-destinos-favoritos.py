# Crie uma lista de locais que você gostaria de conhecer no mundo, na ordem do local que você dá mais prioridade pra o local que você dá menos prioridade. Exiba a lista nas seguintes configurações:
# 
# a) ordem original
# b) ordem alfabética
# c) ordem de prioridades inversa
# d) quantidade de itens

destinos = []


for d in range(0,10):
    destinos.append(input('Digite locais que você deseja viajar: '))
    resposta = input('você deseja adicionar um local favorito? [s] sim [n] não: ')
    if resposta == 's':
        continue
    else:
        break

# letra a
print(f'\nA - lista na ordem original: {destinos}')

# letra b
print(f'\nB - na ordem alfabética: {sorted(destinos)}')

#  letra c

# letra d
print(f'\nD - para uma quantidade de: {len(destinos)} destinos\n\n')