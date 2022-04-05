# Encontrar números primos é uma tarefa difícil...
# 
# Faça um programa que gera uma lista dos números primos existentes entre 1 e um número inteiro informado pelo usuário.

num = int(input('Digite um Número: '))
primos = []

for i in range(1,num):  # precisa ser maior que 1
    if i % i == 0:
        primos.append(i)
    else:
        continue

print(f'Números Primos no Intervalo: {primos}')