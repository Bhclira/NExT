# Implemente um programa que possa receber do usuário a temperatura em graus Celsius ou Fahrenheit. Antes de receber a temperatura, pergunte ao usuário se ele deseja inserir em Celsius ou em Fahrenheit. Se a entrada for em graus Celsius, o programa deverá retornar a temperatura em Fahrenheit. Se a entrada for em Fahrenheit, o programa deverá retornar a temperatura em Celsius. F = C x 1,8 + 32

opcao = int(input('\nOLÁ!\n Para Inserir em Celsius, digite [1] para FarenHeit [2]: '))
temp = int(input('\nDigite a Temperatura: '))

def celsius_farenheit(temperatura):
    print (f'\nTemperatura Convertida em FarenHeit: {(temperatura*1.8) + 32}\n')

def farenheit_celsius(temperatura):
        print (f'\nTemperatura Convertida em Celsius: {(temperatura-32) / 1.8}\n')


if opcao == 1:
    celsius_farenheit(temp)

elif opcao == 2:
    farenheit_celsius(temp)