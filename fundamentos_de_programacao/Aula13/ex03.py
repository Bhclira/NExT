# vetores

# substituir valor = vetor[i] = novo_valor
# adicionar valor = vetor.append(novo_valor)
# ordenar crescente = vetor.sort()
# ordem decrrscente = vetor.sort(reverse=True)
# contagem de valores: len(vetor)
# Adicionar valor a indice específico: vetor.insert(i, valor)
# remover último valor: vetor.pop()
# remover valor específico: vetor.pop(i)
# remover valor conteúdo: vetor.remove(valor)

# criando vetor
valores = [4, 7, -23, 67]

# substituindo valor
valores[2] = 8
print(valores)

# adicionando novo valor
valores.append(1)
print(valores)

# adicionando em um índice específico
valores.insert(0, 100)
print(valores)

# ordem crescente
valores.sort()
print(valores)

# ordem descrescente
valores.sort(reverse=True)
print(valores)

# contar valores
print (len(valores))

# remover ultimo valor pelo indice
valores.pop()
print(valores)

# remover valor específico pelo índice
valores.pop(2)
print(valores)

# remover valor pelo conteúdo
valores.remove(4)
print(valores)