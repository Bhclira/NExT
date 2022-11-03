'''
Uma ONG está desenvolvendo uma aplicação para cadastro de voluntários, para
isso irão realizar um teste amostral com quatro pessoas. Dentre os dados que
serão cadastrados para cada uma delas, existe idade e a quantidade de horas
semanais dedicadas a ONG. Na sequência apresente:

a) Em binário, a maior idade entre os voluntários;
b) Em hexadecimal, quantas pessoas irão dedicar 4h ou mais semanais;
c) A média de idade das pessoas com 3 casas decimais.
'''

listanomes = []
listaidades = []
listahoras = []

for i in range(2):
    nome = input(f'Digite nome {i+1}: ')
    listanomes.append(nome)
    idade = int(input(f'Digite Idade {i+1}: '))
    listaidades.append(idade)
    horas = int(input(f'Digite quantas horas de trabalho: {i+1}: '))
    listahoras.append(horas)

# letra A - Em binário, a maior idade entre os voluntários
maioridade = max(listaidades)
print(f'\nMaior idade Em Binário: {maioridade:b}')

# letra B - Em hexadecimal, quantas pessoas irão dedicar 4h ou mais semanais;
count = 0
for horas in listahoras:
    if horas >= 4:
        count += 1
print(f'Total de Pessoas + de 4 horas: {count} . em Binário: {count:x}')

# letra C - A média de idade das pessoas com 3 casas decimais.
mediaidade = sum(listaidades)/len(listaidades)
print(f'Media de Idades Formatada: {mediaidade:.3f}')