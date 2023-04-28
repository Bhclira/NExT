'''
5 values input
receive 5 distances for each
output: name, jumps, jumps-media
the program must be closed when the user digite "Sair"
'''

nome = True
contador = 1

saltos = []
while True:
    
    nome = input('Digite seu nome: ').capitalize()
    print(f'Atleta: {nome}')
    
    for i in range(5):
        
            print(i+1, 'o. Salto')
            distancia = float(input('Digite a distância em metros do salto: '))
            saltos.append(distancia)
            
    opc = input('Digite se quer continuar [S/N]')

    media = sum(saltos)/len(saltos)
    
    if opc in 'Nn':
        break

print('\n\t****Resultado****')
print('Atleta: ', nome)

for i in range(5):
        
        print(f'{i+1}o. Salto: {saltos[i]}m')
        contador +=1

print(f'\nMédia dos saltos de {nome} é: {round(media,1)}m')
print('\n')


