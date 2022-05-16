'''
Você está organizando um evento e deseja que os seus convidados se sintam importantes. Sendo assim, quando cada convidado chega ao local você pergunta o nome dele e digita no computador. Então o nome dele é exibido em um painel luminoso na entrada do salão. A mensagem que aparece é: "Seja muito bem-vindo Fulano de Tal, onde Fulano de Tal é o nome da pessoa que chegou.
'''

str = input()

if len(str) <= 120:
    print(f'Seja muito bem-vindo {str}')
else:
    print('Informe um nome com menos de 121 caracteres')
