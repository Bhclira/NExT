valores = [0, 2, 3, 4, 6, 8, 10]

valores.insert(1, 1)
valores.insert(-1,9)

print(valores)

for p, v in enumerate(valores):
    print(f'Na Posição {p} encontrei o valor {v}')