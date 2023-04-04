import math

n = int(input("Digite o numero de vezes que vai rodar o programa: "))

for i in range(0,n):

    
    a = int(input("Digite o valor de A: "))
    if a!=0:

        b = int(input("Digite o Valor de B: "))
        c = int(input("Digite o Valor de C: "))

        delta = b**2 - 4 * a * c
        if delta<0:
            print('Não existem raízes reais com DELTA negativo')
        
        elif delta == 0:
            print('Apenas uma raíz real com DELTA igual a zero')
        
        elif delta > 0:
            x1 = (-b+math.sqrt(delta))/2*a
            x2 = (-b-math.sqrt(delta))/2*a

            print(f'Raiz primeira = : {x1}')
            print(f'Raiz primeira = : {x2}')

    
