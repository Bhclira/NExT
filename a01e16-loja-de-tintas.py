'''
* LOJA DE TINTAS
* faça um programa que peça o tamanho em metros quadrados da área a ser pintada
* considere a cobertura da tinta de 1 litro para cada 3 metros quadrados
* considere que a tinta é vendida em latas de 18 litros, que custam R$ 80 reais
* informar ao usuário a quantidade de latas de tinta a serem compradas e o preço total
* somente sao vendidos numero INTEIRO de latas
'''
import math # importada para arredondar para cima, caso a area a ser coberta resulte em menos de uma lata

areaCobrir = float(input('\nDigite a área a ser pintada em metros quadrados: '))

volumePorLata = 18.0 # litros
valorPorLata = 80.0 # reais

areaCobertura = areaCobrir / 3 # quantos litros precisa

quantasLatas = areaCobertura / volumePorLata

if quantasLatas <= 1:
    quantasLatas = math.ceil(quantasLatas) # arredondar para o inteiro imediatamente acima
    print(f'\n\nA quantidade de latas necessárias é: {quantasLatas} lata(s)\n')
else:
    quantasLatas = math.ceil(quantasLatas) # arredondar para o inteiro imediatamente acima
    print(f'\n\nA quantidade de latas necessárias é: {quantasLatas} lata(s)\n')

print(f'Com um valor total em R$ de: {(quantasLatas * valorPorLata):.2f}\n')

'''
* nesse problema aprendi a utilizar as propriedades da biblioteca "math"
* chamando a biblioteca através da sintaxe "import math"
* para chamar o método de arredondar pra cima "math.ceil(float)"
* pode-se arredondar pra baixo com o método "math.floor(float)"
* obs: no lugar do número o python admite a variável do tipo float também
'''