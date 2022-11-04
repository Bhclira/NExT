'''
* faça um programa que colete quanto se ganha por hora e número de horas trabalhadas no mês
* considere os descontos:
11% para IR
8% para INSS
5% para Sindicato
*
* fazer programa que nos dê:
A - salário bruto
B - quanto pagou ao INSS
C - quanto pagou ao Sindicato
D - o salário líquido
E - calcule os descontos e o salário líquido, conforme a tabela fornecida
'''

valorHora = float(input('\nDigite o valor da sua hora de trabalho: '))
horasTrabalhadas = int(input('Digite a quantidade de horas trabalhadas no mês: '))

salarioBruto = valorHora * horasTrabalhadas
impostoRenda = salarioBruto * 0.11
inss = salarioBruto * 0.08
sindicato = salarioBruto * 0.05
salarioLiquido = (salarioBruto - impostoRenda - inss - sindicato)

print(f'\n+ Salário Bruto: R$ {salarioBruto}')
print(f'- IR (11%) : R$ {impostoRenda}')
print(f'- INSS (8%) : R$ {inss}')
print(f'- Sindicato (5%) : R$ {sindicato}')
print(f'= Salário Líquido : R$ {salarioLiquido}\n')