'''
crie tupla com 5 itens string, então: 
a) acesse e escreva na tela a segunda posição
b) acesse intervalo e escreva na tela da terceira a quinta posição.
c) verifique uma ocorrência na tupla
d) verifique boolean se há ítem na tupla, retorne
e) retorne a posição de um elemento na tupla
f) adicione um elemento na sua tupla criada
'''

tupla_modelo = ()

for i in range (6):
    x = input(f'Escreva nome {i+1}: ')
    tupla_modelo = tupla_modelo + tuple([x]) # adiciona elemento i na tupla vazia

print(tupla_modelo)

# A
print(tupla_modelo[2])
# B
print(tupla_modelo[2:5]) # nao-inclusivo a ultima posição do intervalo assinalado
# C
print(tupla_modelo.count('breno')) # retorna inteiro número ocorrências

# D
print('breno' in tupla_modelo)

# E
print(tupla_modelo.index('breno')) # retorna o inteiro correspondente à posição

# F
tupla_dois = tupla_modelo + ('oligofredo', ) # não entendi a vírgula
print(tupla_dois)