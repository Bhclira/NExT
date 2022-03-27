# Faça um programa em que troque todas as ocorrencias de uma letra L1 pela letra L2 em uma string. A string e as letras L1 e L2 devem ser fornecidas pelo usuario.

palavra = input('\nDigite uma palavra: ')

print(f'A palavra fornecida foi: {palavra}')

resp1 = input('\nDigite a letra a ser substituida: ')
resp2 = input('Digite a letra que será posta no lugar: ')

for i in range(0, len(resp1)):
    palavra = palavra.replace(resp1, resp2)

print(palavra)

# tive problemas: minha forma natural foi essa de baixo:
#
# ocorrencia = palavra.find(resp1)
# resultado = palavra + palavra[ocorrencia].replace(resp1, resp2)
# print(resultado)