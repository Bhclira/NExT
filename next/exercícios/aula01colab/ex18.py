'''
Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).
'''

tamanhoArq = float(input('Digite o Tamamnho do arquivo em MegaBytes: '))
velocidadeArq = float(input('Digite a velocidade de transmissão do arquivo em MegaBytez por segundo: '))
# calcular tempo EM MINUTOS

tempoSegundos = tamanhoArq/velocidadeArq

tempoMinutos = tempoSegundos/60

print(f'/nO tempo calculado em MINUTOS foi de: {tempoMinutos:.4f} minutos aproximadamente')
