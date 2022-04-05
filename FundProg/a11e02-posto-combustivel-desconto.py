# posto de combustivel
# pergunte [1] Gasolina [2] Alcool
# até 10 l, desconto 3 por cento
# acima de 10 e até 20 l, desconto de 5 por cento
# acima de 20 l, desconto de 7 por cento
# alcool 5 reais o litro
# ate 10 litros, desconto de 4 por cento
# acima de 10 l e até 20 l, desconto de 6%
# acima de 20 l, desconto de 8


tipo = int(input('\nEscolha o Combustível [1] gasolina [2] alcool: '))
qtde_litros = int(input('\nQuantos litros você deseja? '))
valor = 0.0
valor_final = 0.0

if tipo==1:
    valor = 6.0
    if qtde_litros<10:
        valor_final = valor * qtde_litros
        valor_final = valor_final - (valor_final*0.03)
    elif qtde_litros>=10 and qtde_litros<20:
        valor_final = valor * qtde_litros
        valor_final = valor_final - (valor_final*0.05)
    else:
        valor_final = valor * qtde_litros
        valor_final = valor_final - (valor_final*0.07)
elif tipo==2:
    valor = 5.0
    if qtde_litros<10:
        valor_final = valor * qtde_litros
        valor_final = valor_final - (valor_final*0.04)
    elif qtde_litros>=10 and qtde_litros<20:
        valor_final = valor * qtde_litros
        valor_final = valor_final - (valor_final*0.06)
    else:
        valor_final = valor * qtde_litros
        valor_final = valor_final - (valor_final*0.08)
else:
    print('\nDigite o numero [1] para gasolina, ou [2] para alcool.')

print(f'\nO preço final foi R$ {valor_final}\n')




