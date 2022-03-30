# imprime pares no intervalo de dois numeros
# peça num ini e num fin
import os
os.system("cls")

num1 = int(input('Digite o numero inicial: '))
num2 = int(input('Digite o numero final: '))
count = 0

while num1<=num2:
    if num1%2==0:
        count+=1
    num1 = num1 +1

print('\nExistem,', count, 'numeros pares')
