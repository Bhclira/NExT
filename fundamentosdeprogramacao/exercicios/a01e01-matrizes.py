'''
'''

matriz = [[], []]

for linha in range(2):
    for coluna in range(4):
        matriz[linha].append(int(input('')))

for linha in range(2):
    for coluna in range(4):
        print(f'[{matriz[linha][coluna]:⁴}]', end="")
