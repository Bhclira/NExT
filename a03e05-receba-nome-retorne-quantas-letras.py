# Digite um nome, calcule e retorne quantas letras tem esse nome.
# Quantos espaços detectados.
#

txt = input('Digite um nome: ')

print(len(txt) - txt.count(" "))
# comando/parâmetro count elimina os espaços, casa haja.

print(len(txt.replace(' ','')))
# replace localiza e substitui dentro da string os parâmetros fornecidos .replace(parametro1, parametro2)

aux = txt.split()
print(aux)
# .split retorna uma lista de substrings dividido por um separador.

print(len(''.join(aux)))
# .join concatena strings