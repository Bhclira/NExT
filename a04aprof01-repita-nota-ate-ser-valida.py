# Faça um programa que peça uma nota, entre zero e dez.
# Mostre uma mensagem caso o valor seja inválido e
# continue pedindo até que o usuário informe um valor válido.

nota = float(input('Digite Sua Nota [nota entre 0 e 10]: '))

while nota<0 or nota>10:
  print(f'{nota} é uma nota INVÁLIDA')
  nota = float(input('Digite uma Nota entre 0 e 10: '))

print(f'sua nota {nota} é VÁLIDA')