'''
ex08 - Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês
'''

valorHora = float(input('\nBem-vindo! Digite o valor da sua hora trabalhada: '))
quantidadeDeHoras = int(input('Digite a quantidade de horas trabalhadas no mês: '))

salarioTotal = valorHora*quantidadeDeHoras

print(f'\nO salário calculado foi de: R$ {salarioTotal}\n')


