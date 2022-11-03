# Desenvolva um programa que leia o comprimento de três retas
# e informe ao usuário se elas podem ou não formar um
# triângulo.
# 
# obs. condição para ser um triângulo é que uma das
#       retas seja maior que a soma das outras duas.

lado1 = float(input('\nTamanho do LADO 1: '))
lado2 = float(input('\nTamanho do LADO 2: '))
lado3 = float(input('\nTamanho do LADO 3: '))

if lado1>lado2+lado3 or lado2>lado1+lado3 or lado3>lado1+lado2:
    print(f'\n  os tamanhos fornecidos representa um TRIÂNGULO')
else:
    print(f'\n  os tamanhos fornecidos NÃO representa um TRIÂNGULO')