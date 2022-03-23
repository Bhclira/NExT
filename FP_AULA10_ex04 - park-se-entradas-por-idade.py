idade = int(input("Digite sua idade: "))

if (idade < 4) or (idade > 60):
    print('Entrada gratuita')
elif idade > 4 and idade < 18:
    print ("A estrada custa R$ 20")
else:
    print ("O valor do ingresso é R$ 30")
