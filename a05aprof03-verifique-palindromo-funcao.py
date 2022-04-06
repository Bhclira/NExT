# Um palíndromo é uma palavra que se soletra da mesma forma nos dois sentidos, como “osso” e “reviver”.
# Escreva um função que dado uma plavra verifique se ela é palindro.

palavra = input('Digite uma Palavra: ')
palavraInvertida = palavra[::-1]

def verificador (palavra1, palavra2):
    if palavra1 == palavra2:
        return True
    else:
        return False

print(f'Resultado Verificador Para Palíndromo: {verificador(palavra, palavraInvertida)}')