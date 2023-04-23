"""
Selection Sort Algorithm

"""

matrix = [[],[],[],[]]

for l in range (4): # linha trimestre
    for c in range (5): # colunas regiões
        matrix[l].append(int(input(f"Digite valor para posição [(linha)] [(coluna)]: ")))

# print matriz
for l in range (4):
    for c in range (5):
        print(f'[{matrix[l][c]:^4}]', end="")
    print()

print(m[1][2][3][4])