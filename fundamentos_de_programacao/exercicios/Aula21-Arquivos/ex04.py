'''
Crie arquivo usando metodo W, dentro de uma função gerarListaOrdenada.
Usando um iterador da lista ordenada, inclua no arquivo os elementos da lista.
Feche o arquivo.

obs.: converta de numero para string para que o comando write funcione.

'''

def gerarListaOrdenada():
    quantidade = int(input('Informe a quantidade de elementos: '))
    arquivo = open('idsOrdenados.txt', 'w')

    for elemento in range(quantidade):
        arquivo.write(str(elemento)+"\n")

    arquivo.close()