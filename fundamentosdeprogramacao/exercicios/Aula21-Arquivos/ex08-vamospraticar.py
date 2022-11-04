'''
Crie um programa simples que pergunta se a pessoa deseja ler um
arquivo ou escrever algo nele."

Nosso script vai funcionar assim:
Aparece um menu de opções (sair, ler ou escrever). Se digitar ler, lê
o conteúdo do arquivo e exibe na tela.
Se optar por escrever, escreve algo no arquivo.
'''

import os.path

op=1
while op:
    if os.path.isfile('teste.txt') is false:
        print('Arquivo teste.txt não existe. Criando ...')
        meuArquivo = open('teste.txt', 'w')
    
    meuArquivo = open('teste.txt', 'r+')

    print('\n\tMenu de Opções\n')
    op=int(input('0. sair \n'
                    '1. Ler\n'
                    '2. Escrever\n'
                    '\nEscolha sua Opção: '))
    
    if op == 1:
        print('\n', meuArquivo.read())
        meuArquivo.close()
    
    elif op==2:
        meuArquivo = open('teste.txt', 'a')
        num = input('Digite um numero: ')
        meuArquivo.write(num + '\n')
        meuArquivo.close()

meuArquivo.close()