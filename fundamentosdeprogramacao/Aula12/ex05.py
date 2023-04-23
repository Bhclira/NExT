'''
Após o usuário digitar um número inteiro, informe se ele é um número perfeito.
Um número é perfeito se a soma dos seus divisores (exceto ele) for igual ao
próprio número. Ex: : 6 é perfeito, pois 1+2+3 = 6.
'''

print('VAMOS VERIFICAR SE UM NÚMERO DIGITADO É PERFEITO!')

acumulador = 0
num = int(input('Digite um número inteiro: '))

for i in range(1, num):
    if num % i == 0:
        acumulador += i 

if acumulador == num:
    print(f'O número digitado [{num}] é perfeito!')
else:
    print(f'O número digitado [{num}] NÃO é perfeito!')

print('\nFinal do Programa.')
