
nome = str(input('\nDigite seu primeiro nome: '))

idade = int(input('Digite sua idade: '))



if (idade >= 65):
    
    print('\nAtendimento com prioridade\n')
    
    contagio = str(input('Se você possui alguma doença infecto-contagiosa no momento, responda (S/N): '))
    contagio = contagio.upper()

    if (contagio == 'S'):
        print('\nEncaminhe-se para a sala amarela\n')
    else:
        print('\nEncaminhe-se para a sala branca\n')
else:
    
    print('\nAtendimento sem prioridade\n')
    contagio = str(input('Se você possui alguma doença infecto-contagiosa no momento, responda (S/N): '))
    contagio = contagio.upper()

    if (contagio == 'S'):
        
        print('\nEncaminhe-se para a sala amarela\n')
    
    else:
        
        print('\nEncaminhe-se para a sala branca\n')
