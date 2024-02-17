'''
* Faça aum programa que calcule a área de um quadrado
* em seguide mostre o dobro dessa área para o usuário
'''

print('\n' + 'Olá! Vamos alcular a área de um quadrado qualquer!\n')
base = float(input("Digite o primeiro lado do quadrado: "))
altura = float(input("Digite a altura do quadrado: "))

area = (base * altura)

print('\n' + 'A área do quadrado foi calculada: ', area, '\n')
print('\n' + 'O dobro dessa área, então: ', (area*2), '\n\n')