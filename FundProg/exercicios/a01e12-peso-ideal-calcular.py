'''
* tendo os dados de altura de uma pessoa, construa:
* algoritmo que calcule seu peso ideal
* usando a formula: "((72.7 * altura) - 58)"
'''

print('\nOlá! Vamos calcular seu peso ideal!\n')
altura = float(input('Digite sua altura em centímetros: '))

pesoIdeal = (72.7 * altura) - 58

print(f'\nSeu peso ideal é: {altura:.2f} kilogramas\n')

'''
* essa fórmula está bizarra e o resultado não é realista
* conferi mais de uma vez e está tudo ok com a lógica dos operadores
 tanto para metros quanto para centímetros
* usei o limitados de casas decimais para float na saída do dado
'''