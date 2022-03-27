# Entre com um nome e imprima o nome somente se a primeira letra do nome for “a” (maiuscula ou minuscula).

txt = input('Digite um nome: ')

print(txt[0])

if (txt[0]=='a') or (txt[0]=='A'):
    print(f'{txt}')
else:
    print(f'> {txt} < não se inicia por caracter a ou A.')

# logica alternativa:
if (txt[0].lower()=='a'):
    print(txt)