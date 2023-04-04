from datetime import date

ano_atual = date.today().year

cont_maior = 0
cont_menor = 0
for i in range (0, 5, 1):
    ano = int(input('Digite o ano de seu nascimento: '))

    if (ano_atual - ano >= 18):
        cont_maior +=1
    else:
        cont_menor+=1

print(f'Número de maiores de idade é: {cont_maior}')
print(f'Número de menores de idade é: {cont_menor}')

