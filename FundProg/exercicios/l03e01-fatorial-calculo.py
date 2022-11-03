# Faça um programa que peça ao usuário que insira um número
# inteiro e calcule o seu fatorial. O fatorial é a multiplicação do
# número escolhido até 1.
#   Exemplo:
#    o fatorial de 5 é 120
#       (5x4x3x2x1 = 120).
#           Entrada de dados: 5
#           Saída de dados: 120

num = int(input('Digite um Número para Fatorial: '))

contador = 1
resultado = 1

while (contador<=num):
    resultado = resultado * contador    # acumulador
    contador += 1

print(f'{resultado}')