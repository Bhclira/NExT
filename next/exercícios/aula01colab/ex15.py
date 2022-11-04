'''
ex15 - Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.

Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:

a. salário bruto.
b. quanto pagou ao INSS.
c. quanto pagou ao sindicato.
d. o salário líquido.
e. calcule os descontos e o salário
f. líquido, conforme a tabela abaixo:

'''

valorHora = float(input('\nDigite o valor da sua hora trabalhada: '))
horasTrabalhadas = int(input('Digite a quantidade de horas que você trabalhou no mês atual: '))

salarioBruto = valorHora*horasTrabalhadas
impostoRenda = salarioBruto*(11/100)
impostoPrevidencia = salarioBruto*(8/100)
impostoSindicato = salarioBruto*(5/100)
salarioLiquido = salarioBruto-impostoRenda-impostoPrevidencia-impostoSindicato

print(f'\n+ Salário Bruto: R$ {salarioBruto}')
print(f'- IR (11%): R$ {impostoRenda}')
print(f'- INSS(8%): R$ {impostoPrevidencia}')
print(f'- Sindicato(5%): R$ {impostoSindicato}')
print(f'= Salário Líquido: R$ {salarioLiquido}\n')
