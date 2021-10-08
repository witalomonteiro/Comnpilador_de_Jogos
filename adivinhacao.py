import random


def jogar():
    print("***************************************")
    print("**** Bem-Vindo ao Adivinhação v1.1 ****")
    print("***************************************")

    rodada = 0
    random.seed()
    nivel = ""
    pontos = 100

    print("Qual nível de dificuldade?")
    nivel = int(input("[1] Fácil    [2] Médio   [3] Difícil\n"))

    if nivel == 1:
        tentativas = 7
        numero_secreto = random.randint(1, 10)
    elif nivel == 2:
        tentativas = 5
        numero_secreto = random.randint(1, 20)
    elif nivel == 3:
        tentativas = 3
        numero_secreto = random.randint(1, 30)
    else:
        print("Opção Inválida!")

    for rodada in range(1, tentativas + 1):
        print(f"Tentativa {rodada} de {tentativas}")
        palpite = int(input("Digite seu palpite: "))
        if numero_secreto != palpite:
            if rodada == tentativas:
                print("Errou Novamente! Fim de Jogo!\n")
            elif palpite < numero_secreto and tentativas > 0:
                print("Você Errou! Na proxima, tente um pouco mais!\n")
            elif palpite > numero_secreto and tentativas > 0:
                print("Você Errou! Um pouco menos na proxima!\n")
            pontos = pontos - abs(numero_secreto - palpite)
        else:
            print(f"Você Acertou! Sua pontuação foi {pontos} pontos!\n")
            break

if (__name__ == "__main__"):
    jogar()