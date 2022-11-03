'''

Escreva a Função LeiaInt incluindo a Possibilidade de escrita de um Número de Tipo Inválido

Aproveite e crie também a função LeiaFloat com a mesma funcionalidade

'''
def leiaInt(msg):
    while True:
        n1 = str(input(msg))
        if n1.isnumeric():
            valor = int(n1)
            break
        else:
            print('ERRO! digite um número inteiro válido.')
            n1 = input('Digite: ')
    
    return valor

def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
            
        except (ValueError, TypeError):
            print('ERRO! Digite Numero Real Válido: ')
            continue
        except (KeyboardInterrupt):
            print('O Usuário Interrompeu a Entrada de Dados.')
            return 0
        else:
            return n


# num1 = leiaInt('Digite um número inteiro: ')
num2 = leiaFloat('Digite um número decimal: ')

print(f'O Valor Digitado Real foi {leiaFloat(num2)}')

''' modo alternativo para leiaFloat
    # while True:
    #     n2 = str(n)
    #     if n2.isdecimal():
    #         valor = float(n2)
    #         break
    #     else:
    #         print('ERRO! digite um número decimal válido.')
    #         n = input('Digite: ')
    
    # return valor

'''