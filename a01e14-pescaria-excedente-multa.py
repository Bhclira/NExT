'''
* pescador comprou computador para calcular o resultado diário do seu trabalho
* toda vez que ele traz um peso maior que o regulamento de pesca permite (50kg)
* deve pagar multa de 4,0 reais por kg excedente.
* faça um programa que leia a variável peso (peso de peixes) e calcule o excesso.
* grave na variável "excesso" a qtde em kg além do limite
* e na variável "multa", o valor da multa que deverá pagar
* imprima os dados do programa de maneira adequada
'''

pesoPeixe = float(input('\nDigite o peso pescado no dia de hoje: '))
limitePeso = float(50)

if pesoPeixe > limitePeso:
    excesso = float(pesoPeixe - 50)
    print(f'\nConstatamos um excedente hoje de: {excesso} kilogramas')

else:
    excesso = 0
    print(f'\nExcedente legal não constatado.\nA pescaria rendeu peso dentro dos limites legais. ')

print(f'\nO valor da multa para a pescaria do dia foi de R$: {float(excesso * 4.0)}' + ' reais\n')


