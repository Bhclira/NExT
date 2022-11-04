# Crie um programa que possua uma lista de nomes.
# Peça que o usuário insira um nome que será buscado nesta lista.
# A busca deve ser implementada em uma função que retorna os valores lógicos verdadeiro ou falso.

nomes = ['breno', 'thais', 'tania', 'luciana', 'dasha', 'vermelho']
nome = input('\nDigite um Nome Para a Busca: ')

def busca(lista_parametros, nome_busca):
    for n in lista_parametros:
        if n == nome_busca:
            return True
        else:
            return False

print(busca(nomes, nome))