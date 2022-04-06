# Faça uma função que receba um valor inteiro e positivo e calcule o seu fatorial.

num = int(input('\nDigite Número Inteiro e Positivo: '))

def calcule_fatorial(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n > 1:
        resultado = 1
        for i in range(1,n+1):
            resultado = resultado * i
        return resultado
          
print('\nResultado Fatorial para {num}: ')
print(calcule_fatorial(num))