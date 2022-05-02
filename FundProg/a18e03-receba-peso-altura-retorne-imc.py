'''
receba de 5 pessoas o peso e altura, calcule o IMC
imprima os IMCs aproximados utilizando duas casas decimais
imprima a porcentagem de pessoas acima da media do IMC
utilize print formatado
'''

for i in range(5):
    peso = float(input(f'Digite peso {i+1}'))
    altura = float(input(f'Digite Altura {i+1}'))
    imc = peso/(altura**2)
    print(f'IMC {i+1} = {imc:.2f}')