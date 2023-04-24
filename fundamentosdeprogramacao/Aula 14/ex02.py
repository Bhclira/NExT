'''
5 values input
receive 5 distances for each
output: name, jumps, jumps-media
the program must be closed when the user digite "Sair"
'''

nome = True
contador = 1
saltos = []

while nome != "Sair":
    print('Atleta', contador)
    nome = input('Digite seu nome: ').capitalize()
    if nome == "Sair":
        break
    else:
        for i in range(5):
            print(i+1, 'o. Salto')
            distancia = float(input('Digite a distância em metros do salto: '))
            saltos.append(distancia)
    
    media = sum(saltos)/len(saltos)

    print('\n\t****Resultado****')
    print('Atleta: ', nome)

    for i in range(5):
        print(i+1, 'o. Salto: ',saltos[i], 'm')
    
    print('Média dos saltos ', round(media,1), 'm')
    print('\n')
    contador +=1


