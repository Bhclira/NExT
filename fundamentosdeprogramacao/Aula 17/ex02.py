# n:n*n

dicionario = {}

num = int(input('Digite um número: '))

for i in range(num+1):
    dicionario[i] = i**2

print(dicionario)