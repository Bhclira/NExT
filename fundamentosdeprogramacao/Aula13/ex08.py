lista = [3.5,6.7,1.0,4.9]

# a -> adicione valor 2.3 na posição 1
lista.insert(1, 2.3)
print(lista)

# b -> remova último valor da lista
lista.pop()
print(lista)

# c -> substitua o valor do indice 2 por 9.2
lista[2] = 9.2
print(lista)

# d -> ordene crescente
lista.sort()
print(lista)

# e -> printe a qtd de valores dessa lista
print(len(lista))

# f -> printe a lista com os novos valores mostre indice e valor

for p, v in enumerate(lista):
    print(f'Na posição {p}, encontra-se valor {v}')