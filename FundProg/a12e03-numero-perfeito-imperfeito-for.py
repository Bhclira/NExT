# Após o usuário digitar um número inteiro, informe se ele é um número perfeito.
#
# Um número é perfeito se a SOMA dos seus divisores (exceto ele)
#   for igual ao próprio número.
#   Exemplo: 6 é perfeito, pois 1+2+3 = 6.

numero = int(input('\nDigite Seu Número a Verificar: '))
soma = 0

for i in range(1, numero):
    if numero%i==0:
        soma += i

print(f'\nA soma dos Divisores deu: {soma}\n')

if soma == numero:
    print(f'O Número Digitado {numero} é PERFEITO\n')
else:
    print(f'O Número Digitado {numero} NÃO é PERFEITO\n')