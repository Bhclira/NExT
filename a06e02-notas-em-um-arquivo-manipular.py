# Crie um programa que registra as notas de uma pessoa na escola (como o boletim)
#   em um arquivo.
# 
# Em seguida, leia todos os valores para imprimir o menor valor, o maior e a média.
#   Dica: Se você usar listas, pode usar as funções min() e max().

lista = [8.6 ,7.6 ,9.5 ,4.5 ,9.8 ,10 ]

with open ('/home/brenoman/Documentos/GitHub/NExT/NExT/Arquivos/notas.txt', 'w') as notas:
    for nota in lista:
        notas.write(str(nota) + '\n')

with open ('/home/brenoman/Documentos/GitHub/NExT/NExT/Arquivos/notas.txt') as notas:
      lista2=[] # crie uma Lista Vazia Secundária
      soma = 0  # crie e inicialize um Acumulador
      for linha in notas:
          soma = soma + float(linha)   # adiciona os VALORES de cada linha ao Acumulador
          lista2.append(float(linha))   #acrescenta os valores de cada linha na lista vazia Lista2

# A.1
print(f'\nMédia das Notas Contidas no Arquivo: {sum(lista2)/len(lista2):.2f}')

# A.2
print(f'\nA Menor Nota Encontrada: {min(lista2)}')

# A.3
print(f'\nA Maior Nota Encontrada: {max(lista2)}')

print('\n Fim do Programa \n')