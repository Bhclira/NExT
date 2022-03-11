'''
* peça uma data e verifique a validade da mesma
'''
print('\nVamos Verificar se a data é Válida!\n')

dia = int(input('\nDigite o dia: '))
mes = int(input('Digite o mês: '))
ano = int(input('Digite o ano: ')) # caso essa variável nao seja INT type, vai dar erro.

# cirar um mecanismo falso fazer verificação quando as condições estiverem satisfatórias
validade = False

if (mes==1 or mes==3 or mes==5 or mes==7 or mes==8 or mes==10 or mes==12): # meses que têm 31 dias
    if(0<dia<=31):
        validade = True

elif (mes==4 or mes==6 or mes==9 or mes==11): # meses com 30 dias
    if (0 < dia <=30):
        validade = True

elif (mes==2): # fevereiro possui alguns anos com 29 dias: atençâo!
    if((ano%4==0 and ano%100!=0) or (ano%400==0)):
        if(0<dia<=29):
            validade = True

    elif(0<dia<=28):
         validade = True

if (validade): # o compilador interpretou como verdadeiro, caso eu nao especifique "False"
    print(f'\nA data digitada {dia}/{mes}/{ano} é uma data válida!\n')