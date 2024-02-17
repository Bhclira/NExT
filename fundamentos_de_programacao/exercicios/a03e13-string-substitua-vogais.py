# Faça um programa que receba uma palavra e calcule quantas vogais (a, e, i, o, u) possui essa palavra. Entre com um caractere (vogal ou consoante) e substitua todas as vogais da palavra dada por esse caractere.

palavra = input('\nDigite uma palavra qualquer: ')
substituto = input('Digite a letra pela qual queres trocar as vogais: ')

print('\nSubstituindo vogais pelo Substituto, abaixo: \n')

letra = palavra.find('a')
if letra != -1:
    print(palavra.replace(palavra[letra], substituto))

letra = palavra.find('e')
if letra != -1:
    print(palavra.replace(palavra[letra], substituto))

letra = palavra.find('i')
if letra != -1:
    print(palavra.replace(palavra[letra], substituto))

letra = palavra.find('o')
if letra != -1:
    print(palavra.replace(palavra[letra], substituto))

letra = palavra.find('u')
if letra != -1:
    print(palavra.replace(palavra[letra], substituto))

print('\n FIM DO PROGRAMA')