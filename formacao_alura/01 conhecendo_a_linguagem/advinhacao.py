import random

def jogar():
    print("***********************************")
    print("* Bem Vindo ao Jogo de Advinhação *", end="\n")
    print("***********************************")

    numero_serceto = random.randrange(1, 101)
    total_de_tentativas = 0
    pontos = 1000

    print("Qual nível de dificuldade?")
    print("(1) Facil (2)Medio (3)Difícil")

    nivel = int(input("Defina o nível: "))

    if (nivel == 1):
        total_de_tentativas = 20
    elif (nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada,total_de_tentativas))
        chute_str = input("Digite o seu número entre 1 e 100: ")
        print("Voce Digitou", chute_str)
        chute = int(chute_str)

        if (chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if (acertou):
            print("Acertou, miseravi! e fez {} pontos".format(pontos))
            break

        else:
            if (maior):
                print("Você chutou pra cima")

            elif (menor):
                print("Voce chutou pra baixo")
            pontos_perdidos = abs(numero_secreto - chute) #40 -60
            pontos = pontos - pontos_perdidos
        
    print("Fim do Jogo")

if (__name__== "__main__"):
    jogar()