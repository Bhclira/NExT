# escrever um programa em Python que leia um vetor V1 de n posições e gere um vetor V2 de tamanho n que é o vetor V1 invertido.

n = int(input('Digite as Posições da Lista: '))

v1 = list(range(0, n))  #cria uma lista sem valores, só com posições

v2 = v1[:]  # recebe lista criando uma cópia da lista original
v2.reverse()    # reverte a cópia da lista

print(v2)