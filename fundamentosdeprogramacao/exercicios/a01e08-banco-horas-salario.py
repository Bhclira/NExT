'''
* faça um programa que peça quanto voce ganha por hora
* em seguida, o número de horas trabalhadas no mês
* calcule e mostre o total do seu salário no referido mês
'''

valorHora = float(input('\n' + 'Quanto você ganha por hora trabalhada?: '))
horasTrabalhadas = float(input('Quantas Horas você trabalhou esse mês?: '))

salario = (valorHora * horasTrabalhadas)

print('\n' + 'Você receberá nesse mês: R$ ', salario, '\n')