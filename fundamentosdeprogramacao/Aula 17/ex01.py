# palíndromo

frase = str(input('Digite uma frase: ')).upper()

frase = frase.lower()
frase = frase.split(' ')
''.join(frase)

if frase == frase[::-1]:
    print('A frase é um Palíndromo!')
else:
    print('Não é palindromo')
