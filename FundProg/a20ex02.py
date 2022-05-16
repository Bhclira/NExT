num1 = float(input())
num2 = float(input())

def somar():
    resultado = num1 + num2
    print(resultado)

def subtrair():
    resultado = num1 - num2
    print(resultado)

def dividir():
    resultado = num1 / num2
    print(resultado)

def multiplicar():
    resultado = num1 * num2
    print(resultado)

operation = input('Digite a Operação desejada: ')

if operation == '+':
    somar()
elif operation == '-':
    subtrair()
elif operation == '/':
    dividir()
elif operation == '*':
    multiplicar()
else:
    print('Operação nao existente')