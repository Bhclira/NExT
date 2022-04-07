# Aumente a lista de heróis no arquivo herois.txt. Feito isso, crie um programa
# que leia esse arquivo e crie dois novos arquivos:
# 
# A. Um arquivo apenas com heróis da Marvel;
# B. Outro apenas com heróis da DC.
# C. Imprima na tela os Arquivos Resultantes

with open ('/home/brenoman/Documentos/GitHub/NExT/NExT/Arquivos/dc.txt', 'w') as dc:
    with open('/home/brenoman/Documentos/GitHub/NExT/NExT/Arquivos/marvel.txt', 'w') as marvel:
        with open ('/home/brenoman/Documentos/GitHub/NExT/NExT/Arquivos/herois.txt') as arquivo:
            for linha in arquivo:
                if 'DC' in linha:
                    dc.write(linha)     # letra A
                else:
                    marvel.write(linha) # letra B

with open ('/home/brenoman/Documentos/GitHub/NExT/NExT/Arquivos/dc.txt', 'r') as dc:
    print(dc.read())

with open ('/home/brenoman/Documentos/GitHub/NExT/NExT/Arquivos/marvel.txt', 'r') as marvel:
    print(marvel.read())