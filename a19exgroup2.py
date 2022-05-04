'''
faça programa que solicita ao usuário seu nome completo, em seguida printe:

a) quantas letras tem o primeiro nome
b) quantas letras tem o ultimo nome
c) o nome e o primeiro sobrenome,
    com as primeiras letras em maiúsculas
'''

nome = input('Digite seu nome completo: ')
nomeFatiado = nome.split()

# letra A
a = len(nomeFatiado[0])
print (f'Quantas letras tem a primeira palavra: {a}')

# letra B
b = len(nomeFatiado[-1])
print (f'Quantas letras tem a última palavra: {b}')

# letra C
c = " ".join(nomeFatiado[0:2])
print (f'Primeiro nome Concatena Ultimo: {c.title()}')