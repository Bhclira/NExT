# Crie uma lista com os preços dos jogos que você mais gosta.
# a) Imprima o preço mais caro;
# b) Imprima o preço mais barato.
# c) imprima o local da lista do preço mais alto

gamePreco = [10, 20, 30, 80, 90]

print(f'\nO Preço Mínimo Encontrado: {min(gamePreco)}')

print(f'\nO Preço Máximo Encontrado: {max(gamePreco)}')

print(f'\nA Posição no Vetor do Preço Máximo: {gamePreco.index(max(gamePreco))}\n')