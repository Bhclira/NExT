'''

'''

matriz = [[], [], []]
soma = 0.0

for a in range(3):
    for n in range(4):
        matriz[a].append(float(input('Digite a nota {n +1} do aluno {a +1} ')))
        soma+=matriz[a][n]

media = soma/12
media = round(media, 2)

print(f'A média da turma é: {media}')