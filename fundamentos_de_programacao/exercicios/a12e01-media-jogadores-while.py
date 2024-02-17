# Desenvolva um programa que pergunte ao treinador a quantidade de
# jogadores que o seu time possui.
# Após isso, o programa deverá receber a altura de cada um dos jogadores e,
# ao final, informar a altura média do time.

# Se a média for maior que 1.80, informe a mensagem “Time com jogadores
# altos”, senão, “Time com jogadores de estatura mediana”.

jogadores = int(input('\nBem vindo, Treinador!\nDigite a seguir a quantidade de jogadores no seu time: '))

somaDasAlturas = 0
contador = 1

while (contador<= jogadores):
    alturaJogador = float(input('Digite a ALTURA do jogador: '))
    somaDasAlturas = somaDasAlturas + alturaJogador
    contador = contador+1

jogadores = float(jogadores)
mediaDasAlturas = somaDasAlturas/jogadores

if mediaDasAlturas > 1.80:
    print(f'\nPara a MEDIA DE ALTURA {mediaDasAlturas:.2f}, temos: Media de Jogadores ALTA\n')
else:
    print(f'\nPara a MEDIA DE ALTURA {mediaDasAlturas}, temos: Media de Jogadores BAIXA\n')

