'''
adicione uma lista de valores
'''

dados = []
arquivo = open('lista.txt', 'w')

for i in range(5):
    dados.append(input('Digite o nome do voluntário da ONG: '))

arquivo.writelines("\n" .join(dados))