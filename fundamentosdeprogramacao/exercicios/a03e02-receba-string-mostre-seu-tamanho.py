'''
Crie um programa que:

    a) imprima o comprimento de uma STRING
    b) Substitui as ocorrencias de uma substring fornecida pelo usuário por outra encontrada na string original
    c) Converta substrings da sting principal para minúsculas
    d) Por fim, imprima intervalo de index 0 a index 4.

'''


















txt = input('Escreva uma frase qualquer: ')

# LETRA A
print(len(txt))

#LETRA B
print(txt.replace('e', 'u'))
    
'''
    .replace ('paramentro1', 'parametro2') substitui dentro da
        string o parametro1 pelo parametro 2
'''

# LETRA C
print(f'String em Minúscula: {txt.lower()}')

# LETRA D
print(f'Intervalo de index solicitado: {txt[0:4]}')