'''
ex07 - Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
'''

medida = float(input('\nBem-vindos! Vamos calcular o dobro da área de um quadrado perfeito\nDigite o valor do seu lado: '))

dobroDaArea = (medida*medida)*2

print(f'O dobro da área do quadrado de lado {str(medida)} é de: {dobroDaArea}\n')
