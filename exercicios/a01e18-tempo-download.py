'''
* faça um programa que peça:
1. o tamanho de um arquivo em megabyte
2. a velocidade de um link da internet EM MB/S
*
* calcule o tempo aproximado de download EM MINUTOS
*
'''

tamanho = float(input('\nDigite o tamanho do arquivo: '))
velocidade = float(input('\nDigite a velocidade do link: '))

tempoSegundos = tamanho / velocidade
print(f'\nO tempo estimado para o download é: {tempoSegundos} segundos\n')

tempoMinutos = tempoSegundos / 60

print(f'O arquivo será baixado em: {tempoMinutos:.2f} minutos\n')