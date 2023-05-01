# n:n*n

# um dicionário contém uma 'chave' e um 'value' ou alguns 'values' para cada posição
# no dicionário, a chave funciona como um índex para acessar o conteúdo
# inicializa-se o dicionário com chaves {}
# as chaves e valores serão sempre separado por dois pontos ':'

# exemplo: {'Pedro': 92345678}




dicionario = {}

num = int(input('Digite um número: '))

for i in range(num+1):
    dicionario[i] = i**2

print(dicionario)