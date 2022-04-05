# Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.

login = input('Digite seu Nome: ')
senha = input('Digite sua senha: ')

while login==senha:
  print('Nome Fornecido é igual a Senha, tente outra senha: ')
  senha = input('Digite uma Senha Válida: ')

print('Seu Cadastro Foi efetuado com Sucesso!')