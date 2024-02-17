nomes = ["Carol", 'Maria', 'Lucas', 'Artur']

nomes[1] = 'José'
print(nomes)

nomes.append("As")
print(nomes)

nomes.insert(3, "oi")
print(nomes)

nomes.sort()
print(nomes)

nomes.sort(reverse=True)
print(nomes)

nomes.pop()
print(nomes)

nomes.pop(1)
print(nomes)

print(f'Numero de intens da lista: [{len(nomes)}]')

print(nomes)