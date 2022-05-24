'''
Leia um arquivo 'dados.txt', manipule suas strings. Ao final imprima os seus dados, a quantidade de caracteres e sua quantidade de palavras.
'''

import os
os.system("cls")

arquivo = open("dados.txt", 'r')
dados = arquivo.read()
palavras = dados.split()

print('Dados dos Arquivos: \n', dados)
print('Quantidade de caracteres: \n', len(dados))
print('Quantidade de palavras: \n', len(palavras))