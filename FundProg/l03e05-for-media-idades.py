# Utilizando o comando for, desenvolva um programa que
# calcule a média da idade de cinco pessoas.

numPessoas = 5
mediaIdade = 0
contIdade = 0
somaIdade = 0

for pessoas in range(1, (numPessoas+1)):
    idade = int(input('Digite sua Idade: '))
    contIdade += 1
    somaIdade = somaIdade + idade

mediaIdade = (somaIdade/contIdade)
print(f'\nMédia de Idade: {mediaIdade}')