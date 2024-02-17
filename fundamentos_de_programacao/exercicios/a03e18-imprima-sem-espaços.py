# Leia um vetor contendo letras de uma frase inclusive os espaços em branco. Retirar os espaços em branco do vetor e depois escrever o vetor resultante.

frase = 'o rato roeu a roupa do rei de roma'

print(frase.split())

resultante = frase.replace(' ', '')

print(f'\n Aqui está a frase sem espaços: {resultante}')