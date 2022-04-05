# Uma empresa possui 30 funcionários e resolveu oferecer um
# auxílio família de R$ 150,00 por filho. O sistema deverá
# perguntar a quantidade de filhos e informar o valor total do
# bônus para cada funcionário.


numFuncionarios = 30

contador = 1

while contador<=numFuncionarios:
    numFilhos = int(input('\nDigite quantidade de Filhos: '))
    bonus = numFilhos*150
    print(f'Para {numFilhos} filhos, um BONUS de: {bonus}')
    contador+=1