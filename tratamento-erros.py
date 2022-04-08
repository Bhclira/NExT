'''
aula tratamento de erros
'''

'''
n = int(input('Número: '))
print(f'Você digitou o Número {n}')

# se digitar não-inteiro; typeError
'''

try:

    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b

except Exception as erro:
    print(f'Problema Encontrado foi {erro.__class__}')

except(ValueError, TypeError):
    print ('Tivemos Problema com o Tipo de Dados Digitados.')

except KeyboardInterrupt:
    print('O Usuário preferiu Não Informar os Dados.')

except ZeroDivisionError:
    print('Não é Possível Dividir por Zero.')

except Exception as erro:
    print(f'O Erro Encontrado foi: {erro.__cause__}')
    
else:
    print(f'O resultado é {r:.2f}')

finally:
    print('Volte Sempre!')

# se b = 0; zerodivisionError




'''
lst = [3, 6, 4]
print(lst[3])

# se iterador nao existe, IndexError (out of range)
'''

''' FORMA

try:
    'operação'
except:
    'falhou' o que acontece
except:
    'falhou' de novo

else:
    então faça

finally:
    faça finalmente

'''