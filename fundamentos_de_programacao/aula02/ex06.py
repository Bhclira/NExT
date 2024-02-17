idade = int(input('\nDigite sua idade: '))

if idade <=4 or idade >=60:
    print(f'\nEntrada Gratuita')

elif idade > 4 and idade < 18:
    print(f'\nValor da entrada = R$ 20')

elif idade >= 18 and idade:
    print(f'\nValor da entrada = R$ 30')

else:
    "\nDigite uma idade válida"