'''
Peça que o usuário digite três valores inteiros, na sequência exiba:

a) Em binário, o maior número;
b) Em hexadecimal, quantos números são maiores que 5;
c) A média dos três números com 3 casas decimais;
d) O menor número em octal;
e) A média ponderada dos três números com 2 casas decimais:
    1o valor tem peso 2; O 2o peso 4; O 3o peso 6.
'''

listanum = []
count = 0

for i in range(3):
    num = int(input(f'Digite Número {i+1}:'))
    listanum.append(num)

print(listanum)

# letra A - Em binário, o maior número;
maior = max(listanum)
print(f'{maior:b}')

# letra B - Em hexadecimal, quantos números são maiores que 5
for num in listanum:
    if num > 5:
        count += 1
print(f'Números maior(es) que 5: {count}')

# letra C - A média dos três números com 3 casas decimais;
media = sum(listanum)/len(listanum)
print(f'Média Aritmética Obtida: {media:.3f}')

# letra D - O menor número em octal;
menor = min(listanum)
print(f'Menor Número em Octal: {menor:o}')

# letra E - A média ponderada dos três números com 2 casas decimais:
    # 1o valor tem peso 2; O 2o peso 4; O 3o peso 6.
mediapond = listanum[0]*2 + listanum[1]*4 + listanum[2]*6 / (2 * 4 * 6)
print(f'Média Ponderada Obtida: {mediapond:.2f}')