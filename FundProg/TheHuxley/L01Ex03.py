'''
Uma pesquisa sobre algumas características físicas da população de uma determinada região coletou os seguintes dados, referentes a cada habitante, para serem analisados:

Sexo (masculino (m), feminino (f));
Cor dos olhos (azuis (a), verdes (v), castanhos (c));
Cabelos (louros (l), castanhos (c), pretos(p));
Idade em anos.


Para cada habitante, foram digitadas duas linhas, a primeira com a idade e a segunda os outros dados e a última linha, que não corresponde a ninguém, conterá o valor igual a -1.

Escreva um programa que dê a idade do habitante mais velho e a porcentagem de mulheres que tenham idade maior ou igual a 18 e menor ou igual a 35 anos, sejam louras e tenham olhos verdes.

O percentual deve ser calculado considerando-se o total de pessoas e não somente o total de mulheres.
'''
listaIdades = []
listaGenero = []
listaOlhos = []
listaCabelos = []

print('''\nInicialmente Digite sua Idade,
1. Gênero (m ou f):
2. Cor dos Olhos ( a, v ou c):
3. Cor dos Cabelos (l, c, p): 
''')

cont = 0

for i in range(5):
    
    idade = int(input('Idade: '))
    listaIdades.append(idade)

    genero = input('Sexo: ')
    listaGenero.append(genero)
    
    cabelos = input('Cabelos: ')
    listaCabelos.append(cabelos)

    olhos= input('Olhos: ')
    listaOlhos.append(olhos)
    
for i in range(5):
    if listaGenero[i-1] == 'f':
        if listaIdades[i-1] >= 18 and i <= 35:
            if listaCabelos[i-1] == 'l':
                if listaOlhos[i-1] == 'a':
                    cont = cont + 1

total = len(listaIdades)

# A
print(f'Mais Velho: {max(listaIdades)}')
# B
print(f'Mulheres com olhos verdes, loiras com 18 a 35 anos: {cont*100/total:.2f}%')