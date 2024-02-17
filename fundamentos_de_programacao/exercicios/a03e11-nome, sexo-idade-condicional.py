# Ler nome, sexo e idade. Se sexo for feminino e idade menor que 25, imprime o nome da pessoa e a palavra “ACEITA”, caso contrario imprimir “NÃO ACEITA”.

nome = input('\nDigite seu nome: ')
idade = int(input('Digite sua idade: '))
sexo = input('Digite seu gênero [m] masculino ou [f] feminino: ')

if sexo == 'f' and idade < 25:
    print('\nACEITA\n')
else:
    print('\nNÃO ACEITA\n')

print('\n FIM DO PROGRAMA\n')