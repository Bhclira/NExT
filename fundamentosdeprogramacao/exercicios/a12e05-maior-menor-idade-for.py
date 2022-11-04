# Crie um programa que leia o ano de nascimento de cinco pessoas No final,
# mostre quantas pessoas ainda não atingiram a maioridade e quantas já
# são maiores de idade.

# ano_atual = date.today().year

from datetime import date

ano_atual = date.today().year

contMaior = 0
contMenor = 0

for i in range (0,5):
    nascimento = int(input('Digite o Ano do Seu Nascimento: '))
    if ano_atual - nascimento >=18:
        contMaior += 1
    else:
        contMenor += 1

print(f'\nQuantidade de Pessoas MAIORES DE IDADE: {contMaior}')
print(f'Quantidade de Pessoas MENORES DE IDADE: {contMenor}\n')