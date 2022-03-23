num1 = int(input('Digite numero A:'))
num2 = int (input('Digite numero B: '))

soma = num1+num2

if num1+num2 > 10:
    soma = soma + 5
elif soma <=10:
    soma = soma - 5

print(f'Resultado = {soma}')