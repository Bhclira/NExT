'''
Crie uma string chamada 'txt' que receba uma frase qualquer de algumas palavras.
    
    Em seguida, manipule os dados das seguintes maneiras:

    a. Calcule e retorne quantas substrings tem a STRING e escreva na tela a qtde. sem os espaços
    b. Calcule e retorne quantas substrings ao todo.
    c. Calcule as palavras contidas na STRING total, retorne em forma de lista
    d. Concatene as substrings da lista acima e imprima sem espaços na tela
    d. Calcule a partir da string original a string na ordem invertida.

'''






















txt = input('Digite um nome: ')

# letra A
print(len(txt) - txt.count(" "))
# comando/parâmetro count elimina os espaços, casa haja.

print(txt.replace(' ',''))
# replace localiza e substitui dentro da string os parâmetros fornecidos .replace(parametro1, parametro2)

aux = txt.split()
print(aux)
# .split retorna uma lista de substrings dividido por um separador.

print(''.join(aux))
# .join concatena strings

txt_invert = txt[::-1]
print(txt_invert)