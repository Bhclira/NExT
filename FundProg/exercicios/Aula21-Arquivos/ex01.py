'''
Leia um Arquivo 'media.txt' e imprima ao final quantos numeros tem esse arquivo bem como sua média;.
'''

arquivos_numeros = open("media.txt", "r")
soma = 0.0
quant_numeros = 0

for num in arquivos_numeros:
    num = float(num)
    soma+= num
    quant_numeros+=1

arquivos_numeros.close()

media = soma/quant_numeros
print(media)