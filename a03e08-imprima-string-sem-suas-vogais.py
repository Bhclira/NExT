# Faça um programa que receba do usuario uma string. O programa imprime a string sem suas vogais.

palavra = input(str('Digite um nome: '))

vogais = ['a', 'e', 'i', 'o', 'u']

for i in range(0, len(vogais)):
    palavra = palavra.replace(vogais[i], "")

print (palavra)