
print('\n\nEntre com o ano e modelo do carro a seguir.\n Para adicionar um novo veículo,\n responda a pergunta a seguir:\n  ')

contador = 0
mais_novo = 1000
mais_rapido = 0
resposta = 'S'

while (resposta != 'N'):

    ano_carro = int(input('Digite o ano do Carro: '))
    velo_carro = int(input('Digite a sua velocidade máxima: '))

    if ano_carro > mais_novo:
        mais_novo = ano_carro
    
    if velo_carro > mais_rapido:
        mais_rapido = velo_carro
    
    contador = contador + 1

    resposta = str(input('Deseja adicionar novo carro (S/N)'))
    resposta = resposta.upper()

print(f'\nO número de carros: {contador}')

print(f'O ano do carro mais novo foi: {mais_novo}')

print(f'A velocidade do carro mais rápido foi: {mais_rapido}\n')
