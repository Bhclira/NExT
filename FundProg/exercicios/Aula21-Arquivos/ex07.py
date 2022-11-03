import random

def escreverNumerosAleatórios(qtdNumeros, nomeArquivo):
    arquivoNumeros = open(nomeArquivo, 'w')
    for i in range(qtdNumeros):
        arquivoNumeros.write(str(random.randint(0,100)))
        arquivoNumeros.write('\n')

    arquivoNumeros.close()

escreverNumerosAleatórios(100, 'aleatórios.txt')
# parametros da função