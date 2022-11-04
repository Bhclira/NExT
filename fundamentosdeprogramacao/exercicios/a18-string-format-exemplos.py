'''
Solicite um número inteiro como entrada. em seguida formate o mesmo em:

a. decimal
b. binário
c. octal
d. hexadecimal
'''

num = int(input('Informe Número: '))

print(f'''
decimal: {num}
Binário: {num:b}
Octal: {num:o}
Hexadecimal: {num:x}
''')