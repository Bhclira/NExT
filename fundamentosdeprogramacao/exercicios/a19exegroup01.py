'''
Desenvolva um programa que transforme o texto inserido em um texto para capa de um livro
seguindo o formato a seguir:

    a) Autor: as primeiras letras das palavras maiúsculas
    b) Título do livro: todas as letras maiúsculas
    c) subtítulo do livro: as primeiras letras das palavras maiúsculas
    d) Sinopse do livro: Somente primeira letra maiúscula
'''

texto = ['universo em desencanto', 'livro sagrado', 'tim maia', 'era uma vez um universo que desencanto']

# letra A
autor = texto[2].title()
print(f'Autor com primeira letra maiúscula: {autor}')

# letra B
titulo = texto[0].upper()
print(f'Título com primeira letra maiúscula: {titulo}')

# letra C
subtitulo = texto[1].title()
print(f'subtitulo com as primeiras letras maiúscula: {subtitulo}')

# letra D
sinopse = texto[3].capitalize()
print(f'Sinopse com a primeira letra em maiúscula: {sinopse}')