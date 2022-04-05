# A prefeitura de Recife contratou você para desenvolver um
# programa que calcule os valores do IPTU dos imóveis da
# cidade, conforme a área dos mesmos. Pergunte ao usuário a
# quantidade de imóveis que ele deseja calcular o IPTU. Para
# cada um deles, deverá ser inserida a sua área.
#   
#   se a área do imóvel for menor que 200m2, o valor por m2 é de R$1.50
#   
#   se for maior ou igual a 200m2 e menor que 300m2, o valor do m2
#       é de R$2.00
# 
#   se for maior ou igual a 300m2 e menor que 400m2,
#       o valor do m2 é de R$4.00
# 
#   caso contrário, pagará R$5.00 por m2.
# 
# Após a execução de cada loop, exiba o valor do IPTU.

numImoveis = int(input('Digite Quantos Imóveis para Cálculo: '))

for imoveis in range (1, (numImoveis+1)):
    areaImovel = float(input('Area do Imóvel [em metros quadrados]: '))

    if areaImovel<200:
        imposto = areaImovel * 1.50
        print(f'Valor do Iptu: {imposto}')
    
    elif areaImovel>=200 and areaImovel<300:
        imposto = areaImovel * 2.0
        print(f'Valor do Iptu: {imposto}')
    
    elif areaImovel>=300 and areaImovel<400:
        imposto = areaImovel * 4.0
        print(f'Valor do Iptu: {imposto}')
    else:
        imposto = areaImovel * 5.0
        print(f'Valor do Iptu: {imposto}')