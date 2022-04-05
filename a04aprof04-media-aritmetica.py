# Faça um programa que calcule o mostre a média aritmética de N notas.

notas = []
n = int(input('\nDigite a Quantidade de Notas: '))

countNotas = 0
somaNotas = 0

for i in range(1, n+1):
    nota = int(input('Digite sua nota: '))
    notas.append(nota)
    countNotas +=1
    somaNotas = somaNotas + nota

media = somaNotas / countNotas
print(f'\nNotas Digitadas: {notas}')
print(f'A Média de notas foi: {media}')